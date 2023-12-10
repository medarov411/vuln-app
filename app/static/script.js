//Using our API

function login(){
    var uname = document.getElementById("uname").value;
    var passw = document.getElementById("passw").value;

    var dat = {'username':uname, 'password':passw};

    $.ajax('/api/v1.0/storeLoginAPI/',{
        method: 'POST',
        data: JSON.stringify(dat),
        dataType: "json",
        contentType: "application/json",
    }).done(function(res){

      if (res['status'] == 'success'){
        $("#stat").html('<b>Successful Login<b>');
        window.location.href = '/admin-panel?user=' + res.user;
      }
      else{
        $("#stat").html('<b>Login Failed</b>');
      }

    }).fail(function(err){
        $("#stat").html(err);
    });
}

