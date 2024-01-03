#!/usr/bin/node

const request = require('request');

function displayStatusCode (url) {
  request(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

if (process.argv.length === 3) {
  const url = process.argv[2];
  displayStatusCode(url);
}
