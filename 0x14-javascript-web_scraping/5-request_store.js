#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  if (response.statusCode >= 200 && response.statusCode < 300) {
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
