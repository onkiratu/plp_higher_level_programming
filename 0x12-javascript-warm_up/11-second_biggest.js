#!/usr/bin/node

const scores = process.argv;

if (scores.length === 2 || scores.length === 3) {
  console.log(0);
} else {
  let big = scores[0];

  for (let i = 0; i < scores.length; i++) {
    if (scores[i] > big) {
      big = scores[i];
    }
  }

  let secondBig = scores[0];

  for (let i = 0; i < scores.length; i++) {
    if (scores[i] > secondBig && scores[i] < big) {
      secondBig = scores[i];
    }
  }
  console.log(secondBig);
}
