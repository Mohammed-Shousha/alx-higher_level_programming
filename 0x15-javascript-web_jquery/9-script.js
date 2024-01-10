// JavaScript script that displays the value of hello

$(document).ready(function () {
  $.get(
    'https://hellosalut.stefanbohacek.dev/?lang=fr', // the old url is no longer working
    function (data) {
      $('DIV#hello').text(data.hello);
    }
  );
});
