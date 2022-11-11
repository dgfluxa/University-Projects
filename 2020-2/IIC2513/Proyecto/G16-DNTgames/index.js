
var User = localStorage.getItem('user_sesion');
if (localStorage){

  if (User !== null && User) {
    var user = JSON.parse(User);
    }
  else{
    var user = null;
  }
}

function Head(){
    
    if (user !== null) {
        $('#sesion1').append('<a href="src/views/seleccion_partida.html" class="navbar-link">Jugar </a>');
        $('#sesion-cerrar').append('<a id="logout" class="navbar-link">Cerrar Sesión </a>');
        $('#perfil').append('<a href="src/views/perfil.html" class="navbar-link">Perfil </a>');
        $('#bienvenida').append("<div><a href='src/views/perfil.html' class='navbar-link'><h2 id='user'>" + user.username + "</h2></a></div>");
        $('div#imagen').append("<a href='src/views/seleccion_partida.html' class='button'>¡Jugar Ahora!</a>");
    }
    else{
        $('#bienvenida').append("<div>Registrate y comienza a jugar ahora mismo</div>");
        $('#sesion').append('<a href="src/views/iniciar_sesion.html" class="navbar-link">Iniciar Sesión </a>');
        $('#registro').append('<a href="src/views/registro.html" class="navbar-link" >Registrarse </a>');
    }
    var log_out = document.getElementById("logout");
    //console.log(log_out);
    if(log_out!= null){
      log_out.addEventListener("click", recibeListado);
    }

    function enviaRequest(url) {
      const myHeader = {
        "Authorization": "Bearer "+user.token,
        "Content-type":"application/json"
        };
      return fetch(url, {method:"DELETE", headers:myHeader}).then(respuesta => { return respuesta.json() })
      //.then(json => console.log(json))
    }
    
    async function recibeListado(){
      const users = await enviaRequest("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/session/log_out");
      console.log(users);
      localStorage.setItem('user_sesion', JSON.stringify(null))
      $(location).attr('href', "./src/views/iniciar_sesion.html");
    }
}




$(document).ready(Head);







/*
function cerrar_sesion(){
  console.log(user.token);
  const myHeader = {
  "Authorization": "Bearer "+user.token,
  "Content-type":"application/json"
  };
  fetch("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/users")
  .then(respuesta=>{
    console.log(respuesta.json());
    //console.log(respuesta.error);
  })
  .then(dataRespuesta=>{
    console.log(dataRespuesta.error);
  })

  $(location).attr('href', "./src/views/iniciar_sesion.html");
}*/