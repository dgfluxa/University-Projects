var User = localStorage.getItem('user_sesion');
if (localStorage){

  if (User !== null && User) {
    var user = JSON.parse(User);
    }
  else{
    var user = null;
  }
}

$(document).ready(function(){
  /*NAVBAR */
    if (user !== null) {
      $('#sesion1').append('<a href="src/views/seleccion_partida.html" class="navbar-link">Jugar </a>');
      $('#sesion-cerrar').append('<a id="logout" class="navbar-link">Cerrar Sesión </a>');
      $('#perfil').append('<a href="perfil.html" class="navbar-link">Perfil </a>');
    }
    else{
        $('#sesion').append('<a href="iniciar_sesion.html" class="navbar-link">Iniciar Sesión </a>');
        $('#registro').append('<a href="registro.html" class="navbar-link" >Registrarse </a>');
    }
      /* FIN NAVBAR*/
      var log_out = document.getElementById("API");
      console.log(log_out);
      if(log_out!= null){
        log_out.addEventListener("click", crear_user);
      }

    });









function crear_user(){

  var mensajes = document.getElementById("mensaje");
  if ($('#p1').val() != $('#p2').val()) {
      mensajes.innerHTML = "Las constraseñas no coiciden";
  }
  else{
    //aqui habria que mandar el objeto.
    var datos = {
      'username' : document.querySelector('#username').value,
      'password' : document.querySelector('#p1').value,
      'part_g' : 0,
      'part_p' : 0
    }
    fetch("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/users/new",
       { method:"POST", body:JSON.stringify(datos), headers:{"Content-type":"application/json"} })
      .then(responde =>{ return responde.json() })
      .then(dataRespuesta=>{
        if(dataRespuesta.error != undefined){
          mensajes.innerText = dataRespuesta.msg;
       }
      else{
          mensajes.innerText = dataRespuesta.msg;
          if(dataRespuesta.user){
            const user = {
              'username':dataRespuesta.user.username,
              'token': dataRespuesta.user.token,
              'part_g': dataRespuesta.user.part_g,
              'part_p': dataRespuesta.user.part_p
            }
            localStorage.setItem('user_sesion', JSON.stringify(user));
            $(location).attr('href', "../../../index.html");
          }
          //dejamos en local storage el usuario.
          
      }
    })
  }
}
