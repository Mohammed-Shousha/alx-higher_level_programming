#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        completed[todo.userId] = (completed[todo.userId] || 0) + 1;
      }
    });

    console.log(completed);
  }
});
