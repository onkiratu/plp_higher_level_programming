#!/usr/bin/node

const args = process.argv;
function factorial (a) {
  if (a > 0) {
    return a * factorial(a - 1);
  }
  return 1;
}

console.log(factorial(Number(args[2])));
