
const add = document.getElementById('add_item');
add.addEventListener('click', addItem);

function addItem() {
    const ul = document.querySelector('.my_list');
    const li= document.createElement('li');
    li.appendChild(document.createTextNode('Item'));
    ul.appendChild(li);
    };