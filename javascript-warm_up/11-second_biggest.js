#!/usr/bin/node

const process = require('process');
const list = process.argv.sort();
if (list.length > 3) {
  console.log(list[process.argv.length - 2]);
} else {
  console.log('0');
}
