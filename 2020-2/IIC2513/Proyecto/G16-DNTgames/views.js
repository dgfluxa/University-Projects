
var User = localStorage.getItem('user_sesion');
if (localStorage){
  if (User !== null && User) {
    var user = JSON.parse(User);
    }
  else{
    var user = null;
  }
}
$(document).ready(async function(){
    //console.log(user);
    var usuario = await enviaUser("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/users/"+user.username);
    //console.log(usuario.part_g);
    //console.log("helo");
    if (usuario) {
        await (function(usuario){
          if (usuario.part_g > usuario.part_p) {
            $('div.columna-izq').append('<img class="imgRedonda" src="../assets/imgs/Conquistador.PNG"/>');
            $('div.columna-izq').append('<h3 class="perfil"></h3>');
            $('div.columna-izq').append('<div id="description">Tu perfil corresponde a un Conquistador, DNTgames requiere de tu ambición para conquistar. Al igual que Napoleón Bonaparte, tu inteligencia y habilidades de estratega te han llevado a triunfar en la mayoría de tus partidas. Sigue así y conviertete en el mejor jugador.</div>');
          }
          else if (usuario.part_p > usuario.part_g) {
            $('div.columna-izq').append('<img class="imgRedonda" src="../assets/imgs/Renacentista.PNG"/>');
            $('div.columna-izq').append('<h3 class="perfil"></h3>');
            $('div.columna-izq').append('<div id="description">Tu perfil corresponde a un Renancentista, haz perdido algunas partidas que te puede generar dolor, pero recuerda que Nietzsche dijo que el dolor es bueno, te ayuda a crecer y seguir mejorando para ser un mejor conquistador</div>');
          }
          else{
            $('div.columna-izq').append('<img class="imgRedonda" src="../assets/imgs/Pacifista.PNG"/>');
            $('div.columna-izq').append('<h3 class="perfil"></h3>');
            $('div.columna-izq').append('<div id="description">Tu perfil corresponde a un Pacifista, DNTgames necesita gente como tú, así como el mundo necesito a Gandhi, pero todo depende de tí si deseas seguir siendolo, ganando o perdiendo partidas</div>');
          }
        })(usuario);
        $('#sesion1').append('<a href="seleccion_partida.html" class="navbar-link">Jugar </a>');
        $('.perfil').text(user.username)
        $('.win').text(usuario.part_g)/*Aca abría que hacer  un click evento con este botoncito */
        $('.lost').text(usuario.part_p)
        $('#sesion-cerrar').append('<a id="logout" class="navbar-link">Cerrar Sesión </a>');
        $('#perfil').append('<a href="perfil.html" class="navbar-link">Perfil </a>');
        $("#logout").click(recibeListado);
    }
    else{
        $('#sesion').append('<a href="iniciar_sesion.html" class="navbar-link">Iniciar Sesión </a>');
        $('#registro').append('<a href="registro.html" class="navbar-link" >Registrarse </a>');
    }
});

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
  localStorage.setItem('user_sesion', JSON.stringify(null))
  $(location).attr('href', "./iniciar_sesion.html");
}

/*
asy function recibeUser(){
  const url = "https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/users/"+user.username;
  const u = await enviaUser(url);
  return u
}*/

function enviaUser(url){
  const myHeader = {
    "Authorization": "Bearer "+user.token,
    "Content-type":"application/json"
    };
  return fetch(url, {method:"GET", headers:myHeader}).then(respuesta => { return respuesta.json() })
}





//Head();