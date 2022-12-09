#!/usr/bin/node

const process = require('process');

const args = process.argv[2];

if (args) {
  console.log(args);
} else {
  console.log('No argument');
}
