import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
import joblib

def create_or_update_model(data_npz, model_file):

    if os.path.exists(model_file):
        clf, classes = joblib.load(model_file)
    else:
        clf = SVC(kernel='linear', probability=True)
        classes = None


    data = np.load(data_npz)


    X = []
    y = []

    for label, features in data.items():
        for feature in features:
            X.append(feature)
            y.append(label)


    X = np.array(X)
    y = np.array(y)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    if classes is not None: 
        if len(np.unique(y_train)) > 1:
            clf.fit(X_train, y_train)  
        else:
            print("No hay suficientes clases.")
    else:
        if len(np.unique(y_train)) > 1:
            clf.fit(X_train, y_train) 
            print("Modelo creado.")
        else:
            print("No hay suficientes clases.")

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Precisión del modelo: {accuracy * 100:.2f}%')

    joblib.dump((clf, np.unique(y_train)), model_file)
    print("Modelo actualizado")



base_dir = os.path.dirname(__file__)

data_npz = os.path.join(base_dir, 'data_faces.npz')
model_file = os.path.join(base_dir, 'face_features.pkl')


create_or_update_model(data_npz, model_file)
