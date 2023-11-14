#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);

const first = fs.readFileSync(args[0]);
const second = fs.readFileSync(args[1]);

fs.writeFileSync(args[2], first + second);
