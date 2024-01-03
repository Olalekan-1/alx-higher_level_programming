#!/usr/bin/node

const request = require('request');

function displayTitle (titleCode) {
  const url = `https://swapi-api.alx-tools.com/api/films/${titleCode}`;
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const content = JSON.parse(body);
      console.log(content.title);
    }
  });
}

const titleCode = process.argv[2];
if (titleCode) {
  displayTitle(titleCode);
}
