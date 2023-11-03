#!/usr/bin/node

const argv = process.argv;

const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

function add (a, b) {
  const c = a + b;
  console.log(c);
}

add(num1, num2);
