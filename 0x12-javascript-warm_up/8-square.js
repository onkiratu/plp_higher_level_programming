#!/usr/bin/node

const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    for (let j = 0; j < args[2]; j++) {
      console.log('X');
    }
  }
}
