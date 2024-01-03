#!/usr/bin/node
// Prints the number of movies where the character Wedge Antilles is present

const request = require('request');

const url = process.argv[2];
const characterId = '18/';

request(url, (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;

    const count = results.filter((movie) =>
      movie.characters.some((character) => character.endsWith(characterId))
    ).length;

    console.log(count);
  }
});
