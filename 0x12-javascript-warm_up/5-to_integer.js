#!/usr/bin/node
const args = process.argv;

const num = args[2];

if (!isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
