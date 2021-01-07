const showModal = document.querySelector('#showModal')

showModal.addEventListener('click', function() {
    const modalOverlay = document.querySelector("#overlay");
    modalOverlay.classList.toggle("visible");
});