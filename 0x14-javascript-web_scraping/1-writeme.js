#!/usr/bin/node

const fs = require('fs');

function writeAndPrintFile (filePath, string) {
  try {
    fs.writeFileSync(filePath, string, 'utf-8');
  } catch (err) {
    console.log(err);
  }
}

if (process.argv.length === 4) {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeAndPrintFile(filePath, content);
}
