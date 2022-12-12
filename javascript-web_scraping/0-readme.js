#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const fileA = process.argv[2];

fs.readFile(fileA, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
