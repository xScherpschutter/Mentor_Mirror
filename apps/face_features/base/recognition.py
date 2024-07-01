import cv2
import face_recognition
import joblib
import os
def face_features(image_path):
    # Cargar el modelo entrenado y las etiquetas
    model, label = joblib.load(os.path.join(os.path.dirname(__file__), 'face_features.pkl'))

    # Leer la imagen desde el archivo
    image = cv2.imread(image_path)

    # Verificar que la imagen se ha cargado correctamente
    if image is None:
        return "La imagén no se ha cargado correctamente", False, image

    # Detectar las ubicaciones de rostros en la imagen
    face_locations = face_recognition.face_locations(image)
    face_landmarks_list = face_recognition.face_landmarks(image)

    # Verificar si hay exactamente un rostro
    if len(face_locations) != 1:
        return "Solo debe haber un rostro en la imagén!", False, image

    # Procesar el único rostro encontrado
    face_encodings = face_recognition.face_encodings(image, face_locations)
    for face_encoding, face_location in zip(face_encodings, face_locations):
        
        # Predecir el tipo de rostro usando el modelo
        face_type = model.predict([face_encoding])[0]
        face_type = face_type.split('-')[0]

        # Dibujar el rectángulo alrededor del rostro y etiquetarlo
        top, right, bottom, left = face_location
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(image, f'Tipo de rostro: {face_type}', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Dibujar los puntos faciales para el rostro encontrado
    if face_landmarks_list:
        for face_landmarks in face_landmarks_list:
            for facial_feature in face_landmarks.keys():
                points = face_landmarks[facial_feature]
                for point in points:
                    cv2.circle(image, point, 1, (255, 0, 0), -1)

    # cv2.imshow('Landmarks', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return str(face_type), True, image

# Usar la función con una imagen de ejemplo
result, condition, processed_image = face_features('rostro.jpg')
print(result)
print(os.path.join(os.path.dirname(__file__), 'face_features.pkl'))
