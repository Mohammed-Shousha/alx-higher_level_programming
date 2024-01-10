// Javascript script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/'; // the old url is no longer working
  $('INPUT#btn_translate').click(function () {
    $.get(url, { lang: $('INPUT#language_code').val() }, function (data) {
      console.log(data);
      $('DIV#hello').text(data.hello);
    });
  });
});
