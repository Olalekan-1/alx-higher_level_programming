#!/usr/bin/node

const argv = process.argv;

if (argv[2])
{
	const parse = parseInt(argv[2], 10);
	if (!parse)
	{
		console.log("Not a number");
	}
	else
	{
		console.log("My number: " + parse);
	}
}

else
{
	console.log("Not a number");
}


