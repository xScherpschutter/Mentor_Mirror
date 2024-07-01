import face_recognition
import os
import numpy as np

train_dir = os.path.join(os.path.dirname(__file__), 'faces')

face_features = {}

for label in os.listdir(train_dir):
    label_path = os.path.join(train_dir, label)
    
    if os.path.isdir(label_path):

        for filename in os.listdir(label_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                full_path = os.path.join(label_path, filename)
                image = face_recognition.load_image_file(full_path)
                
                face_encodings = face_recognition.face_encodings(image)
                
                if len(face_encodings) == 1:

                    if label not in face_features:
                        face_features[label] = []
                        
                    face_features[label].append(face_encodings[0])
                    
                else:
                    
                    print(f"Se encontró {len(face_encodings)} rostros en {filename}. Solo se necesita 1!")


for label in face_features:
    face_features[label] = np.array(face_features[label])

# Save facial features to a npz file
np.savez(os.path.join(os.path.dirname(__file__), 'data_faces.npz'), **face_features)
print("Características faciales guardadas correctamente.")

