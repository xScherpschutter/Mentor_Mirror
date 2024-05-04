window.addEventListener("DOMContentLoaded", function () {
    var video = document.getElementById('video');
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var snap = document.getElementById('snap');
    var imageDataInput = document.getElementById('imageData');
    var form = document.getElementById('captureForm');
    // form.action = "/optical/" <<< Aquí debe ir la URL de la vista que procesará la imagen (POST method)

    navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        video.srcObject = stream;
    })
    .catch(function(error) {
        console.log("Ha ocurrido un error ", error);
    });

    snap.addEventListener("click", function() {
        context.drawImage(video, 0, 0, 640, 480);
        var imageData = canvas.toDataURL('image/png');
        imageDataInput.value = imageData;
        // console.log("Imagen guardada en el formulario")
        // console.log(imageDataInput.value)
    });
});