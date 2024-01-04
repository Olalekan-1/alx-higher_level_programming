#!/usr/bin/node

const request = require('request');

function displayCharacterOccurrence () {
  let count = 0;
  const url = process.argv[2];

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const content = JSON.parse(body);
      const elem = content.results;
      for (let i = 0; i < elem.length; i++) {
        if (elem[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) { count += 1; }
      }
      console.log(count);
    }
  });
}

if (process.argv.length === 3) {
  displayCharacterOccurrence();
}
