#!/usr/bin/node

let i = 1;

const argv = process.argv;

if (argv[2])
{
	const parse = parseInt(argv[2], 10);
	if (!parse)
	{
		console.log("Missing number of occurrences");
	}
	else
	{
		while (i <= parse)
		{
			console.log("C is fun");
			i++;
		}
	}
}

else
{
	console.log("Missing number of occurrences");
}


