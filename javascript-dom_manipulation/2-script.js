
const redHeader = document.getElementById('red_header');
const header = document.querySelector('header');
redHeader.addEventListener('click', function changeColor(event) {

    event.target.style.color = `#FF0000`;
    header.classList.add('red')
});