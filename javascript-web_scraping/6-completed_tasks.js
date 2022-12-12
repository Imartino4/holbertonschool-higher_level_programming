#!/usr/bin/node

const process = require('process');
const request = require('request');
const url = process.argv[2];

request(url, (error, res, body) => {
  if (error) {
    throw error;
  }
  const list = JSON.parse(body);
  const taskDict = {};
  for (let i = 0; i < list.length; i++) {
    if (list[i].completed === true) {
      if (taskDict[list[i].userId] === undefined) {
        taskDict[list[i].userId] = 1;
      } else {
        taskDict[list[i].userId] += 1;
      }
    }
  }
  console.log(taskDict);
});
