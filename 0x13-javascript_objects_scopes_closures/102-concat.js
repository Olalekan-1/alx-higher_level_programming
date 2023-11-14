#!/usr/bin/node

const fs = require('fs');

const argv = process.argv;

if (argv.length !== 5) {
  console.error('Usage: node concatFiles.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1 = argv[2];
const file2 = argv[3];
const file3 = argv[4];

fs.readFile(file1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(`Error reading file ${file1}: ${err1.message}`);
    process.exit(1);
  }

  fs.readFile(file2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(`Error reading file ${file2}: ${err2.message}`);
      process.exit(1);
    }

    const concat = data1 + data2;

    fs.writeFile(file3, concat, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to file ${file3}: ${err.message}`);
        process.exit(1);
      }
    });
  });
});
