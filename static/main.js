$(document).ready(function(){
  $('#login').click(function() {
    const username = $('#username').val();
    $.post('/login', {
      username:username,
    }).done(function () {
      document.location.reload();
  });
});
  $('#submit').click(function(){
    const message = $('#message').val();
    $.post('/message', { //send a post request to the backend
      message: message
    }).done(function() {
      document.location.reload();
    });
  });
});
