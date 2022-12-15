#!/usr/bin/node

function getAPi() {
    const url = `https://swapi-api.hbtn.io/api/films/?format=json`;
    fetch(url)
    .then((res) => res.json())
    .then((data) => {
        // console.log(data);
        showFilms(data); 
    });
}

getAPi();

function showFilms(data) {

    const ul = document.getElementById('list_movies');
    for (let i = 0; i < data.results.length; i++) {
        const li = document.createElement('li');
        ul.appendChild(li)
        li.innerHTML = data.results[i].title;
    }
}

