#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request(url, (error, res, body) => {
  if (error) {
    throw error;
  }
  fs.writeFileSync(file, body);
});
