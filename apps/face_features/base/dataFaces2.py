import os
import numpy as np
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
import gc

def process_images_in_folder(folder_path):
    try:
        gc.collect()
        # Inicializar MTCNN para la detección de caras
        mtcnn = MTCNN(image_size=160, margin=0, min_face_size=20)

        # Inicializar el modelo InceptionResnetV1 preentrenado
        model = InceptionResnetV1(pretrained='vggface2').eval()

        face_features = {}
        print('Carpeta:', folder_path)
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                full_path = os.path.join(folder_path, filename)
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

                    label = os.path.basename(folder_path)
                    if label not in face_features:
                        face_features[label] = []
                    
                    face_features[label].append(face_encoding[0])
                    
                except Exception as e:
                    print('Error con la imagen {}: {}'.format(filename, e))
                    continue
                
                finally:
                    stats = gc.get_stats()
                    print('Estado de la memoria: ', stats)
                    image.close()
                    del image
                    gc.collect()

        print('Creando archivo npz por carpeta...')
        for label in face_features:
            face_features[label] = np.array(face_features[label])

        # Guardar las características faciales en un archivo npz por carpeta
        np.savez(os.path.join(folder_path, 'data_faces_{}.npz'.format(os.path.basename(folder_path))), **face_features)
        print(f"Características faciales guardadas correctamente en {folder_path}.")

    except Exception as e:
        print('Fatal error: ', e)


if __name__ == "__main__":
    train_dir = os.path.join(os.path.dirname(__file__), 'faces')

    for label in os.listdir(train_dir):
        label_path = os.path.join(train_dir, label)
        
        if os.path.isdir(label_path):
            process_images_in_folder(label_path)