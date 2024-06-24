function closeModal() {
    var modal = document.getElementById("modalDisplay");
    modal.style.display = "none";
}

function openInput() {
  var sendCapture = document.getElementById('sendCapture');
  sendCapture.style.display = 'block'
}

function closeInput() {
  var sendCapture = document.getElementById('sendCapture');
  sendCapture.style.display = 'none'
}

function showSuccessModal(condition) {
var successModal = document.getElementById('successModal');
var successMessage = document.getElementById('successMessage');

if (!condition)  {successMessage.innerText = 'Ha ocurrido un error'; }  

successMessage.innerText = 'Datos enviados correctamente';
successModal.style.display = 'block';
}

function closeSuccessModal() {
var successModal = document.getElementById('successModal');
successModal.style.display = 'none';
}