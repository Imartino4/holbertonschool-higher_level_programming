#!/usr/bin/node

// el link a js está en el head, por lo tanto se carga antes que el html
// hay que agregar el event
document.addEventListener('DOMContentLoaded', function getAPi() {
    const url = `https://stefanbohacek.com/hellosalut/?lang=fr`;
    fetch(url)
    .then((res) => res.json())
    .then((data) => {
        // console.log(data);
        sayHello(data); 
    });
})

function sayHello(data) {
    const div = document.getElementById('hello');
    div.innerHTML = data.hello;
    }
