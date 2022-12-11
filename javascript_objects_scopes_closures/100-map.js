#!/usr/bin/node

const importList = require('./100-data').list;

const newList = importList.map((n, i) => n * i);
console.log(importList);
console.log(newList);
