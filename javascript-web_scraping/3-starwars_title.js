#!/usr/bin/node

const process = require('process');
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

console.log(url);

request(url, (error, res, body) => {
  if (!error) {
    console.log(body.title);
  } else {
    throw error;
  }
});
