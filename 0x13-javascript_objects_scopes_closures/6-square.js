#!/usr/bin/node
const SquareOne = require('./5-square');

class Square extends SquareOne {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('X');
        }
        console.log();
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('c');
        }
        console.log();
      }
    }
  }
}
module.exports = Square;
