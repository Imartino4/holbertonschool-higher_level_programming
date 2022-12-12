#!/usr/bin/node

const process = require('process');
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, res, body) => {
  if (error) {
    throw error;
  }
  const results = JSON.parse(body);
  for (let i = 0; i < results.characters.length; i++) {
    request.get(results.characters[i], (error, res, bod) => {
      if (error) {
        throw error;
      }
      console.log(JSON.parse(bod).name);
    });
  }
});
