#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv
    .map(arg => parseInt(arg))
    .slice(2, process.argv.length)
    .sort((a, b) => b - a);

  console.log(args[1]);
}
