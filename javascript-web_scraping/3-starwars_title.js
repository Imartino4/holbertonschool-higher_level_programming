#!/usr/bin/node

const process = require('process');
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

console.log(url);

request.get(url, (error, res, body) => {
  if (error) {
    throw error;
  }
  console.log(JSON.parse(body).title);
  });
