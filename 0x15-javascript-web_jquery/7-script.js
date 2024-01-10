// JavaScript script that fetches the character name

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
