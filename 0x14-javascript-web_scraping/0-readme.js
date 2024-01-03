#!/usr/bin/node

const fs = require('fs');

function readAndPrintFile (filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (err) {
    console.log(err);
  }
}

if (process.argv.length === 3) {
  const filePath = process.argv[2];
  readAndPrintFile(filePath);
}
