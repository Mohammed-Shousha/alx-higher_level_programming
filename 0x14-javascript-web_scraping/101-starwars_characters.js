#!/usr/bin/node
// Prints all characters of a Star Wars movie in the same order of the list “characters” in the /films/ response

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const printCharacters = (characters, index) => {
  request(characters[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
};

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
