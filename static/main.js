$(document).ready(function(){
  $('#submit').click(function(){
    const message = $('#message').val();
    $.post('/message', { //send a post request to the backend
      message: message
    }).done(function() {
      document.location.reload();
    });
  });
});
