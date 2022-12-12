#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const fileA = process.argv[2];
const textToWrite = process.argv[3];

fs.writeFile(fileA, textToWrite, (err) => {
  if (err) throw err;
});
