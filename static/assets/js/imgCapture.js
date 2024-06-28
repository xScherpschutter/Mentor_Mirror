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

if (!condition)  {
  successMessage.innerText = 'Error!';
  successImage.src = '/static/assets/img/error.gif';

}  

successMessage.innerText = 'Éxito!';
successImage.src = '/static/assets/img/success.gif';
successModal.style.display = 'block';
}

function closeSuccessModal() {
var successModal = document.getElementById('successModal');
successModal.style.display = 'none';
}

function showLoadingModal() {

  const modal = document.createElement('div');
  modal.id = 'loadingModal';
  modal.style.display = 'flex';
  modal.style.position = 'fixed';
  modal.style.zIndex = '1';
  modal.style.left = '0';
  modal.style.top = '0';
  modal.style.width = '100%';
  modal.style.height = '100%';
  modal.style.overflow = 'auto';
  modal.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
  modal.style.justifyContent = 'center';
  modal.style.alignItems = 'center';

  const modalContent = document.createElement('div');
  modalContent.className = 'modal-content';
  modalContent.style.backgroundColor = '#fefefe';
  modalContent.style.margin = 'auto';
  modalContent.style.padding = '20px';
  modalContent.style.border = '1px solid #888';
  modalContent.style.width = '80%';
  modalContent.style.maxWidth = '300px';
  modalContent.style.textAlign = 'center';

  const loaderImg = document.createElement('img');
  loaderImg.src = '/static/assets/img/load.gif'
  loaderImg.alt = 'Espere...';
  loaderImg.style.width = '120px';
  loaderImg.style.height = '120px';

  const text = document.createElement('p');
  text.style.textAlign = 'center'
  text.innerText = 'Espere...';

  modalContent.appendChild(loaderImg);
  modalContent.appendChild(text);
  modal.appendChild(modalContent);
  document.body.appendChild(modal);
}

function hideLoadingModal() {
  const modal = document.getElementById('loadingModal');
  if (modal) {
      modal.remove();
  }
}