#!/usr/bin/node

const argv = process.argv;

if (!argv[2])
{
	argv[2] = "undefined";
}

if (!argv[3])
{
	argv[3] = "undefined";
}

console.log(argv[2] +" is " + argv[3]);
