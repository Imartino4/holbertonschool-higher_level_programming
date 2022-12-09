#!/usr/bin/node

const process = require('process');

function factorial (a) {
  if (a === 1) {
    return 1;
  }
  const NewA = a - 1;
  if (NewA > 0) {
    return a * factorial(NewA);
  }
}

const arg1 = parseInt(process.argv[2]);
const fact = factorial(arg1);
console.log(fact);
