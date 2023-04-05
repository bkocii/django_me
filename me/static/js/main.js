

function hideSuccessMessage () {
    setTimeout(function () {
        var successMessage = document.getElementById('alert');
        if (successMessage) {
            successMessage.style.display = 'none';
        }
    }, 3000);
}



