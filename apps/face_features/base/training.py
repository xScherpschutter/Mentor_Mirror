import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

if __name__ == "__main__":
    data = np.load(os.path.join(os.path.dirname(__file__), 'data_faces_combined.npz'))
    X = []
    y = []

    for label, features in data.items():
        for feature in features:
            X.append(feature)
            y.append(label)

    X = np.array(X)
    y = np.array(y)

    # Convertir las etiquetas a números enteros únicos
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Guardar el mapeo inverso para reconstruir las etiquetas originales
    inverse_label_map = {i: label for i, label in enumerate(label_encoder.classes_)}

    # Convertir a tensores de PyTorch
    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y_encoded, dtype=torch.long)  # Ahora las etiquetas son números enteros

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_tensor, y_tensor, test_size=0.2, random_state=42)

    # Definir las dimensiones del modelo
    input_dim = X.shape[1]  # Número de características de entrada
    print('Numero de caracteristicas de entrada:', input_dim)
    hidden_dim = 100  # Número de neuronas en la capa oculta
    output_dim = len(np.unique(y))  # Número de clases de salida (número único de etiquetas)
    print('Número de clases de salida:', output_dim)

    # Crear una instancia del modelo
    model = nn.Sequential(
        nn.Linear(input_dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, output_dim)
    )

    # Definir la función de pérdida y el optimizador
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Configurar los datos para el DataLoader
    train_dataset = TensorDataset(X_train, y_train)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

    # Entrenamiento del modelo
    num_epochs = 50

    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item() * inputs.size(0)
        
        epoch_loss = running_loss / len(train_loader.dataset)
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}')

    # Evaluación del modelo con el conjunto de prueba
    model.eval()
    with torch.no_grad():
        outputs = model(X_test)
        _, predicted = torch.max(outputs, 1)
        accuracy = torch.sum(predicted == y_test).item() / len(y_test)
        print(f'Precisión del clasificador en el conjunto de prueba: {accuracy:.2f}')

    # Guardar el modelo entrenado
    model_path = os.path.join(os.path.dirname(__file__), 'face_features_pytorch.pth')
    torch.save(model.state_dict(), model_path)
    print(f'Modelo guardado en: {model_path}')

    # Guardar el mapeo inverso para reconstruir las etiquetas originales después
    label_map_path = os.path.join(os.path.dirname(__file__), 'label_map.npy')
    np.save(label_map_path, inverse_label_map)
    print(f'Mapeo inverso guardado en: {label_map_path}')