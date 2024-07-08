import torch
import base64
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
from deepface import DeepFace
import os
import torch.nn as nn
import io

# Inicializar MTCNN para la detección de caras
mtcnn = MTCNN(image_size=160, margin=0, min_face_size=20)

# Inicializar InceptionResnetV1 para la obtención de codificaciones
feature_extractor = InceptionResnetV1(pretrained='vggface2').eval()

# Definir el mismo modelo utilizado para el entrenamiento
input_dim = 512  # Este valor debe ser consistente con el entrenamiento
hidden_dim = 100
output_dim = 5  # Este valor debe coincidir con el número de clases en el entrenamiento

# Crear una instancia del modelo usando nn.Sequential
classifier = nn.Sequential(
    nn.Linear(input_dim, hidden_dim),
    nn.ReLU(),
    nn.Linear(hidden_dim, output_dim)
)

model_path = os.path.join(os.path.dirname(__file__), 'base', 'face_features_pytorch.pth')
label_map_path = os.path.join(os.path.dirname(__file__), 'base', 'label_map.npy')

classifier.load_state_dict(torch.load(model_path))
classifier.eval()

label_map = np.load(label_map_path, allow_pickle=True).item()

def optical_face_features(image_path):
    try:
        # Cargar la imagen usando Pillow
        pil_image = Image.open(image_path)

        # Asegurarse de que la imagen tiene 3 canales (convertir a RGB si tiene 4 canales)
        if pil_image.mode == 'RGBA':
            pil_image = pil_image.convert('RGB')

        # Detectar las caras en la imagen
        face_locations, _ = mtcnn.detect(pil_image)

        if face_locations is None or len(face_locations) == 0:
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='PNG')
            img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
            return "No se detectaron rostros en la imagen", False, img_base64

        if len(face_locations) != 1:
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='PNG')
            img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
            return "Solo debe haber un rostro en la imagen!", True, img_base64

        # Procesar el rostro detectado
        face_tensor = mtcnn(pil_image)

        if face_tensor is None:
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='PNG')
            img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
            return "No se pudo procesar la imagen correctamente", False, img_base64

        face_tensor = face_tensor.unsqueeze(0)

        with torch.no_grad():
            face_encodings = feature_extractor(face_tensor).numpy()

        # Convertir la predicción de vuelta a etiqueta de texto
        face_encodings = torch.tensor(face_encodings, dtype=torch.float32)
        predicted_label = classifier(face_encodings)
        _, predicted_label_idx = torch.max(predicted_label, 1)
        predicted_label = label_map[int(predicted_label_idx)]

        # Convertir la imagen a base64 para mostrarla en la interfaz web, etc.
        img_byte_arr = io.BytesIO()
        pil_image.save(img_byte_arr, format='PNG')
        img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

        return str(predicted_label), True, img_base64

    except Exception as e:
        print('Error óptico:', e)
        return str(e), False, None

def haircut_face_features(image_path):
    try:
        # Cargar la imagen usando Pillow
        pil_image = Image.open(image_path)

        # Asegurarse de que la imagen tiene 3 canales (convertir a RGB si tiene 4 canales)
        if pil_image.mode == 'RGBA':
            pil_image = pil_image.convert('RGB')

        # Detectar las caras en la imagen
        face_locations, _ = mtcnn.detect(pil_image)

        if face_locations is None or len(face_locations) == 0:
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='PNG')
            img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
            return "No se detectaron rostros en la imagen", False, img_base64

        if len(face_locations) != 1:
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='PNG')
            img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
            return "Solo debe haber un rostro en la imagen!", True, img_base64

        face_tensor = mtcnn(pil_image)

        if face_tensor is None:
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='PNG')
            img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
            return "No se detectaron rostros en la imagen", False, None

        face_tensor = face_tensor.unsqueeze(0)

        with torch.no_grad():
            face_encodings = feature_extractor(face_tensor).numpy()

        face_encodings = torch.tensor(face_encodings, dtype=torch.float32)
        predicted_label = classifier(face_encodings)
        _, predicted_label_idx = torch.max(predicted_label, 1)
        predicted_label = label_map[int(predicted_label_idx)]

        results = DeepFace.analyze(img_path=image_path, actions=['race', 'gender'])

        print('Raza: ', results[0]['dominant_race'])
        print('Género: ', results[0]['dominant_gender'])

        race = 'normal' if results[0]['dominant_race'] != 'black' else 'black'
        gender = results[0]['dominant_gender']

        img_byte_arr = io.BytesIO()
        pil_image.save(img_byte_arr, format='PNG')
        img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

        results_list = [
            {
                'face_type': str(predicted_label),
                'race': str(race),
                'gender': str(gender)
            }
        ]

        return results_list, True, img_base64

    except ValueError as e:
        print('DeepFace Error:', e)
        return None, False, None

    except Exception as e:
        print('Error:', e)
        return None, False, None
