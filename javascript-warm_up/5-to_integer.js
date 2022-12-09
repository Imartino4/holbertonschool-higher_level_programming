#!/usr/bin/node

const process = require('process');

const args1 = process.argv[2];
if (parseInt(args1)) {
  console.log(parseInt(args1));
} else {
  console.log('Not a number');
}
