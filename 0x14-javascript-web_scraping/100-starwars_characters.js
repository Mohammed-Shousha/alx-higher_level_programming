#!/usr/bin/node
// Prints all characters of a Star Wars movie

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, (error, response, content) => {
        if (!error) {
          console.log(JSON.parse(content).name);
        }
      });
    });
  }
});
