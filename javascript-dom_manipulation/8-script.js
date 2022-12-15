#!/usr/bin/node

function getAPi() {
    const url = `https://fourtonfish.com/hellosalut/?lang=fr`;
    fetch(url)
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
        sayHello(data); 
    });
}

getAPi();

function sayHello(data) {

    const div = document.getElementById('hello');
    const p = document.createElement('p');
    div.appendChild(p)
    p.innerHTML = data.hello;
    }

