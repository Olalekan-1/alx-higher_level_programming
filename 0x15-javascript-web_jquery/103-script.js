/* global $ */

$(document).ready(function () {
  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      method: 'GET',
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  }
});
