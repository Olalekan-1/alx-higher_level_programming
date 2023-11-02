#!/usr/bin/node

const argv = process.argv;

let num1 = parseInt(argv[2]);
let num2 = parseInt(argv[3]);

function add(a, b)
{
	c = a + b;
	console.log(c);
}

add(num1, num2);
