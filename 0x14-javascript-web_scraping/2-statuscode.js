#!/usr/bin/node
// Displays the status code of a GET request.

const request = require('request');

const url = process.argv[2];

request
  .get(url)
  .on('response', (response) => console.log(`code: ${response.statusCode}`));
