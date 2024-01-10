// JavaScript script that fetches and lists the title for all movies

$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $('UL#list_movies').append(
      ...data.results.map((movie) => `<li>${movie.title}</li>`)
    );
  });
});
