/* global $ */

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      const movieList = $('#list_movies');
      data.results.forEach(function (movie) {
        movieList.append('<li>' + movie.title + '</li>');
      });
    }
  });
});
