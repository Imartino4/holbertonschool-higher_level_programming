#!/usr/bin/node

const process = require('process');
const list = [];
for (let i = 2; i < process.argv.length; i++) {
  list.push(parseInt(process.argv[i]));
}
if (list.length > 1) {
  list.sort(function (a, b) {
    return a - b;
  });
  console.log(list[list.length - 2]);
} else {
  console.log('0');
}
