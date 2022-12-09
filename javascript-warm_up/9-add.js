#!/usr/bin/node

const process = require('process');

function add (a, b) {
  return a + b;
}

const arg2 = process.argv[3];
const arg1 = process.argv[2];
if (parseInt(arg2) && parseInt(arg1)) {
  const sum = add(parseInt(arg2), parseInt(arg1));
  console.log(sum);
} else {
  console.log('NaN');
}
