#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];

  while (list.length > 0) {
    reversed.push(list.pop());
  }

  return reversed;
};
