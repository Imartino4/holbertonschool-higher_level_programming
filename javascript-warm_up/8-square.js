#!/usr/bin/node

const process = require('process');
const args = process.argv[2];

// One loop
if (parseInt(args)) {
  'X'.repeat(parseInt(args));
  for (let i = 0; i < args; i++) {
    console.log(Array(parseInt(args) + 1).join('X'));
  }
} else {
  console.log('Missing size');
}

// Two loops
// if (parseInt(args)) {
//   let row = 'X'
//   for (let i = 0; i < args - 1; i++) {
//     row = row + 'X';
//   }
//   for (let i = 0; i < args; i++) {
//     console.log(row);
//   }
// } else {
//   console.log('Missing size');
// }
