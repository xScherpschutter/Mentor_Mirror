import os
import numpy as np
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
import gc

try:
    # Inicializar MTCNN para la detección de caras
    mtcnn = MTCNN(image_size=160, margin=0, min_face_size=20)

    # Inicializar el modelo InceptionResnetV1 preentrenado
    model = InceptionResnetV1(pretrained='vggface2').eval()

    train_dir = os.path.join(os.path.dirname(__file__), 'faces')

    face_features = {}

    for label in os.listdir(train_dir):
        label_path = os.path.join(train_dir, label)
        
        if os.path.isdir(label_path):
            for filename in os.listdir(label_path):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    full_path = os.path.join(label_path, filename)
                    print("Imagen:", filename)
                    image = Image.open(full_path)

                    try:
                        # Detectar las caras en la imagen
                        face_locations, _ = mtcnn.detect(image)

                        if face_locations is None or len(face_locations) != 1:
                            print(f"Se encontró {len(face_locations) if face_locations is not None else 0} rostros en {filename}. Solo se necesita 1!")
                            continue

                        # Obtener el tensor de la cara
                        face_tensor = mtcnn(image)
                        if face_tensor is None:
                            print(f"No se pudo procesar la imagen correctamente: {filename}")
                            continue
                        
                        face_tensor = face_tensor.unsqueeze(0)
                        
                        with torch.no_grad():
                            face_encoding = model(face_tensor).numpy()

                        if label not in face_features:
                            face_features[label] = []
                        
                        face_features[label].append(face_encoding[0])
                        
                    except Exception as e:
                        print('Error con la imagen {}: {}'.format(filename, e))
                        continue
                    
                    finally:
                        image.close()
                        del face_tensor, image
                        gc.collect()

    print('Creando archivo npz...')
    for label in face_features:
        face_features[label] = np.array(face_features[label])

    # Guardar las características faciales en un archivo npz
    np.savez(os.path.join(os.path.dirname(__file__), 'data_faces.npz'), **face_features)
    print("Características faciales guardadas correctamente.")

except Exception as e:
    ('Fatal error: ', e)
