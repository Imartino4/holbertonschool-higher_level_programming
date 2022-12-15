#!/usr/bin/node

function getAPi() {
    const url = `https://swapi-api.hbtn.io/api/people/5/?format=json`;
    fetch(url)
    .then((res) => res.json()) //Convierto la respuesta a json
    .then((data) => {
        showName(data); 
    });// Podria definir aca la funcion en lugar de crear una nueva
}

getAPi();

function showName(character) {

    const c = document.getElementById('character');
    const char = document.createElement('p');
    c.appendChild(char)
    char.innerHTML = character.name;
}

