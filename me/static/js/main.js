const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

function hideSuccessMessage () {
    setTimeout(function () {
        var successMessage = document.getElementById('alert');
        if (successMessage) {
            successMessage.style.display = 'none';
        }
    }, 3000);
}
// setTimeout(function () {
//     $('#message').fadeOut('slow');
// }, 3000);