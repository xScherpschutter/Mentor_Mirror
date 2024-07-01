import cv2
import face_recognition
import joblib
import os
import base64
from deepface import DeepFace

def optical_face_features(image):
    try:
        model, label = joblib.load(os.path.join(os.path.dirname(__file__), 'base', 'face_features.pkl'))
        image = cv2.imread(image)

        if image is None:
            return "La imagén no se ha cargado correctamente", False, None

        face_locations = face_recognition.face_locations(image)
        face_landmarks_list = face_recognition.face_landmarks(image)

        if len(face_locations) == 0:
            _, img_encoded = cv2.imencode('.png', image)
            img_base64 = base64.b64encode(img_encoded).decode('utf-8')
        
            return "No se detectaron rostros en la imagen", False, img_base64
        
        if len(face_locations) != 1:
            face_encodings = face_recognition.face_encodings(image, face_locations)
            
            for face_encoding, face_location in zip(face_encodings, face_locations):
                top, right, bottom, left = face_location
                cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                
            _, img_encoded = cv2.imencode('.png', image)
            img_base64 = base64.b64encode(img_encoded).decode('utf-8')

            return "Solo debe haber un rostro en la imagén!", True, img_base64
        
        face_encodings = face_recognition.face_encodings(image, face_locations)
        for face_encoding, face_location in zip(face_encodings, face_locations):
            
            face_type = model.predict([face_encoding])[0]
            face_type = face_type.split('-')[0]
            
            top, right, bottom, left = face_location
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(image, f'Tipo de rostro: {face_type}', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)


        if face_landmarks_list:
            for face_landmarks in face_landmarks_list:
                for facial_feature in face_landmarks.keys():
                    points = face_landmarks[facial_feature]
                    for point in points:
                        cv2.circle(image, point, 1, (255, 0, 0), -1)

        _, img_encoded = cv2.imencode('.png', image)
        img_base64 = base64.b64encode(img_encoded).decode('utf-8')
        
        return str(face_type), True , img_base64
    
    except Exception as e:
            return str(e), False, None
     
def haircut_face_features(image):
    try: 
        image_copy = image
        model, label = joblib.load(os.path.join(os.path.dirname(__file__), 'base', 'face_features.pkl'))
        
        if image is None:
            return "La imagén no se ha cargado correctamente", False, None
        
        image = cv2.imread(image)
        
        face_locations = face_recognition.face_locations(image)
        face_landmarks_list = face_recognition.face_landmarks(image)

        if len(face_locations) == 0:
            _, img_encoded = cv2.imencode('.png', image)
            img_base64 = base64.b64encode(img_encoded).decode('utf-8')
        
            return "No se detectaron rostros en la imagen", False, img_base64
        
        if len(face_locations) != 1:
            face_encodings = face_recognition.face_encodings(image, face_locations)
            
            for face_encoding, face_location in zip(face_encodings, face_locations):
                top, right, bottom, left = face_location
                cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                
            _, img_encoded = cv2.imencode('.png', image)
            img_base64 = base64.b64encode(img_encoded).decode('utf-8')

            return "Solo debe haber un rostro en la imagén!", True, img_base64
                
        face_encodings = face_recognition.face_encodings(image, face_locations)
        for face_encoding, face_location in zip(face_encodings, face_locations):
            
            face_type = model.predict([face_encoding])[0]
            face_type = face_type.split('-')[0]
            
            top, right, bottom, left = face_location
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(image, f'Tipo de rostro: {face_type}', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)


        if face_landmarks_list:
            for face_landmarks in face_landmarks_list:
                for facial_feature in face_landmarks.keys():
                    points = face_landmarks[facial_feature]
                    for point in points:
                        cv2.circle(image, point, 1, (255, 0, 0), -1)
                        
        results = DeepFace.analyze(img_path=image_copy, actions=['race', 'gender'])
        
        print('Raza: ', results[0]['dominant_race'])
        print('Genero: ', results[0]['dominant_gender'])
        
        race = 'normal' if results[0]['dominant_race'] != 'black' else 'black'
        gender = results[0]['dominant_gender']

        _, img_encoded = cv2.imencode('.png', image)
        img_base64 = base64.b64encode(img_encoded).decode('utf-8')
        
        results_list = [
            {
                'face_type' : str(face_type),
                'race' : str(race),
                'gender': str(gender)
            }
        ]
        
        return results_list, True , img_base64
    
            
    except ValueError as e:
        print('Deepface Error')
        return None, False, None
    
    except Exception as e:
        return None, False, None