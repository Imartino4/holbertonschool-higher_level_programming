#!/usr/bin/node

const process = require('process');
const fs = require('fs') // Allow work with file system(read, wirte, etc.)
const fA = process.argv[2].toString(); //File to read and copy
const fB = process.argv[3].toString(); // File to read and copy
const fC = process.argv[4]; //File to create and write

//readFileSync ya retorna el contenido

fs.writeFileSync(fC, fs.readFileSync(fA) + '\n' + fs.readFileSync(fB));
