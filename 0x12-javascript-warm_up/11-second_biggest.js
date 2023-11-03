#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  let i = 0;
  const args = [];

  for (i = 2; i < argv.length; i++) {
    const arg = parseInt(argv[i]);
    if (arg) {
      args.push(arg);
    }
  }

  args.sort(function (a, b) { return a - b; });

  console.log(args[args.length - 2]);
}
