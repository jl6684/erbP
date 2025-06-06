const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(() => {
    $('.alert').fadeOut();
    $('#message').fadeOut();
}, 8000);