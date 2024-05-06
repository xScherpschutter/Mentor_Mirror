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
    });

    sendCapture.addEventListener("click", function() {
        var imageData = canvas.toDataURL('image/png');
        sendImage(imageData);
    });
});

function sendImage(imageData) {
    fetch('/face_features/', {  
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
        const img = data.image
        const face_type = data.message

        showModal(img, face_type) 
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
function showModal(imageData, face_type) {
    try {
        const decodedImage = atob(imageData);
        const imageUrl = 'data:image/png;base64,' + btoa(decodedImage);
        openModal(imageUrl, face_type);

    } catch (error) {
        console.error("Error al decodificar la imagen: ", error)
        alert("Error en la decodificación de la imagen")
    }
}
