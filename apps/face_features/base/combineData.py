import os
import numpy as np

def combine_npz_files(output_file, npz_files):
    combined_data = {}

    for file in npz_files:
        data = np.load(file)
        for label in data.files:
            if label not in combined_data:
                combined_data[label] = data[label]
            else:
                combined_data[label] = np.concatenate((combined_data[label], data[label]))

    np.savez(output_file, **combined_data)
    print(f"Todos los archivos npz combinados correctamente en {output_file}.")
    
if __name__ == "__main__":
    train_dir = os.path.join(os.path.dirname(__file__), 'faces')
    npz = []
    
    for label in os.listdir(train_dir):
        label_path = os.path.join(train_dir, label)
        
        for filename in os.listdir(label_path):
            if filename.endswith(".npz"):
                full_npz_path = os.path.join(label_path, filename)
                npz.append(full_npz_path)
                
    combine_npz_files(os.path.join(os.path.dirname(__file__), 'data_faces_combined.npz'), npz)
    
    data = np.load(os.path.join(os.path.dirname(__file__), 'data_faces_combined.npz'))

    # Acceder a los datos almacenados bajo una etiqueta específica
    for label in data.files:
        print(f"Etiqueta: {label}")
        print(data[label])

