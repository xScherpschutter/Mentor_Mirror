window.addEventListener("DOMContentLoaded", function () {
    var video = document.getElementById('video');
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var snap = document.getElementById('snap');
    var sendCapture = document.getElementById('sendCapture');

    navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        video.srcObject = stream;
    })
    .catch(function(error) {
        console.log("Ha ocurrido un error: ", error);
        alert(error)
    });

    snap.addEventListener("click", function() {
        context.drawImage(video, 0, 0, 640, 480);
        sendCapture.style.display = "block";
    });

    sendCapture.addEventListener("click", function() {
        var imageData = canvas.toDataURL('image/png');
        sendImage(imageData);
        sendCapture.style.display = 'none'
    });
});

function sendImage(imageData) {
    fetch('/face_features/haircut/', {  
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            image: imageData
        })
    })
    .then(response => response.json())
    .then(data => {

        if (!data.success) { alert("Error al recibir la imagén del servidor"); return}

        face_shape = data.data[0].face_type
        race = data.data[0].race
        gender = data.data[0].gender
        img = data.image

        showModal(img, face_shape, race, gender) 

    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Próximamente se deberá editar esta función junto con openModal para iterar los datos en JSON
async function showModal(imageData, face_type, race, gender) {
    try {
        const decodedImage = atob(imageData);
        const imageUrl = 'data:image/png;base64,' + btoa(decodedImage);
        const haircuts = await get_haircuts(face_type, race, gender)

        if (haircuts == null) { alert("No se recibio data"); return }

        openModal(imageUrl, face_type, haircuts);

    } catch (error) {
        console.error("Error al decodificar la imagen: ", error)
        alert("Error en la decodificación de la imagen")
    }
}

async function get_haircuts(face_type, race, gender) {
    try {
        const response = await fetch('/haircut/haircuts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                face_shape: face_type,
                race: race,
                gender: gender
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('fetch realizado:', data);
        return data;

    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}

function openModal(imageUrl, face_type, data) {
    try {
      var modal = document.getElementById("modalDisplay");
      var title = document.getElementById("modalTitle").querySelector("h5")

      modal.style.display = "block"
      var modalImg = document.getElementById("modalImage");

      modalImg.src = imageUrl;
      var dataContainer = document.getElementById("dataContainer");
      dataContainer.innerHTML = '';
      title.innerHTML = "Tipo de rostro: " + face_type

      if (data.data == null ) {
        console.log('No hay datos dentro de data')
        return
      }

      console.log(data.data)

      data.data.forEach(element => {
        var dataImg = document.createElement("img");
        dataImg.src = element.image;
        dataImg.alt = element.name;
        dataImg.style.width = "100px";
        dataImg.style.height = "auto";
        dataImg.style.margin = "10px";
    
        // Crear el elemento de nombre
        var dataName = document.createElement("p");
        dataName.innerText = element.name;
        dataName.style.textAlign = "center";
    
        // Crear un botón
        var button = document.createElement("button");
        button.innerText = "Seleccionar";
        button.style.marginTop = "5px";
        button.dataset.token = element.token;  // Usar un token en lugar de un ID directo
        button.onclick = function() {
            sendHaircut(element.token);
        };
    
        // Crear un contenedor para cada lente
        var dataItem = document.createElement("div");
        dataItem.style.display = "inline-block";
        dataItem.style.textAlign = "center";
    
        // Añadir la imagen, el nombre y el botón al contenedor del lente
        dataItem.appendChild(dataImg);
        dataItem.appendChild(dataName);
        dataItem.appendChild(button);
    
        // Añadir el contenedor del lente al contenedor principal
        dataContainer.appendChild(dataItem);
    });

    } catch (error) {
      console.error('ERROR:', error)
    }
  }

  async function sendHaircut(token) {
    try {
        const response = await fetch('/haircut/save_haircut/', {  
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ token: token })
        });

        const data = await response.json();
        console.log('Success:', data);

        closeModal()
        showSuccessModal(data.success)

    } catch (error) {
        console.error('Error:', error);
    }
}