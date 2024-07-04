import torch
from torchvision import transforms
from PIL import Image
import os

# Definir la ruta al modelo guardado
model_path = os.path.join(os.path.dirname(__file__), 'face_features.pkl')
image_path = r'C:\Users\crows\OneDrive\Documentos\Programacion\MentorMirror\apps\face_features\base\faces\Corazon\heart (1).jpg'

# Función para cargar el modelo
def load_model(model_path):
    model = torch.load(model_path, map_location=torch.device('cpu'))  # Cargar en CPU si es necesario
    model.eval()  # Establecer en modo de evaluación
    return model

# Función para cargar y preprocesar la imagen
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((160, 160)),  # Redimensionar a 160x160
        transforms.ToTensor(),          # Convertir a tensor
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normalización si es necesaria
    ])
    
    img = Image.open(image_path)
    img_tensor = transform(img).unsqueeze(0).float()  # Agregar dimensión batch y convertir a float32
    return img_tensor

# Función para realizar la predicción
def predict(model, img_tensor):
    with torch.no_grad():
        output = model(img_tensor)
    return output

if __name__ == "__main__":
    # Cargar el modelo
    model = load_model(model_path)
    
    # Preprocesar la imagen
    img_tensor = preprocess_image(image_path)
    
    # Realizar la predicción
    prediction = predict(model, img_tensor)
    
    # Mostrar la salida (predicción)
    print("Predicción del modelo:")
    print(prediction)