#!/usr/bin/node

const process = require('process');
const request = require('request');
const url = process.argv[2];
const charId = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, res, body) => {
  if (error) {
    throw error;
  }
  const results = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < results.length; i++) {
    for (let j = 0; j < results[i].characters.length; j++) {
      if (results[i].characters[j] === charId) {
        console.log(results[i].characters[j]);
        count++;
      }
    }
  }
  console.log(count);
});
