#!/usr/bin/node

const list = require('./100-data.js').list;

console.log(list);

const list2 = list.map((x, i) => x * i);
console.log(list2);
