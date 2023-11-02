#!/usr/bin/node

let i = 1;
let j = 1;

const argv = process.argv;

if (argv[2])
{
	const parse = parseInt(argv[2], 10);
	if (!parse)
	{
		console.log("Missing size");
	}
	else
	{
		for (i = 1; i  <= parse; i++)
		{
			for (j = 1; j <= parse; j++)
			{
				process.stdout.write("X");
			}
			console.log()
		}
	}
}

else
{
	console.log("Missing size");
}


