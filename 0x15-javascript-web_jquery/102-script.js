/* global $ */

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      method: 'GET',
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  });
});
