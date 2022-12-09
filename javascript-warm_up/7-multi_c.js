#!/usr/bin/node

const process = require('process');

const args = process.argv[2];
if (parseInt(args)) {
  for (let i = 0; i < args; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
