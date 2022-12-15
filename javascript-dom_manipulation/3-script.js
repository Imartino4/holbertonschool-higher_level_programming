
const tog = document.getElementById('toggle_header');
const header = document.querySelector('header');
tog.addEventListener('click', function changeColor() {

    header.classList.toggle('red')
    header.classList.toggle('green')
});