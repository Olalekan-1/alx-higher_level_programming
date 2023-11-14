#!/usr/bin/node

let count = 0;
exports.logMe = function (item) {
  // let count = 0;
  console.log(count + ': ' + item);
  count++;
};
