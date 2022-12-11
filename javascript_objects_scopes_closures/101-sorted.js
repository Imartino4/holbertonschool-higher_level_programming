#!/usr/bin/node

const importDict = require('./101-data').dict;

const newDict = {};

for (const [k, v] of Object.entries(importDict)) {
  if (v in newDict) {
    newDict[v].push(k);
  } else {
    newDict[v] = [k];
  }
}
console.log(newDict);
