#!/usr/bin/node

exports.esrever = function (list) {
  const myList = [];
  for (let i = 0; i < list.length; i++) {
    myList.unshift(list[i]);
  }
  return myList;
};
