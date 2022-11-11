var Local = localStorage.getItem('usuarios');
var User = localStorage.getItem('user_sesion');
var Jug_hist = localStorage.getItem('jug_historicos');
var jug_hist = [];
if (localStorage){
  if (Local !== null && Local) {
    var Users = JSON.parse(Local);
    }
  else{
    var Users = [];
  }
  if (User !== null && User) {
    var user = JSON.parse(User);
    }
  else{
    var user = null;
  }
  if (Jug_hist !== null && Jug_hist) {
    var jug_hist_actual = JSON.parse(Jug_hist);
    }
  else{
    var jug_hist_actual = [];
  }
}

function obtener_usuarios(url){
  return fetch(url)
  .then(respuesta => { return respuesta.json() })
}

$( document ).ready(async function() {
    var fecha = new Date();
    if (Users.length == 0) {
      var usuarios_db = await obtener_usuarios("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/Users/");
      for (let index = 0; index < usuarios_db.length; index++) {
        var fecha_user = new Date(usuarios_db[index].createdAt);
        if (fecha_user.getDate() == fecha.getDate()) {
          Users.push(usuarios_db[index].username);
        }
      }
    }
    console.log(Users);
    if (user !== null) {
        $('#sesion1').append('<a href="seleccion_partida.html" class="navbar-link">Jugar </a>');
        /*Aca abría que hacer  un click evento con este botoncito */
        $('#sesion-cerrar').append('<a href="iniciar_sesion.html" class="navbar-link">Cerrar Sesión </a>');
        $('#perfil').append('<a href="perfil.html" class="navbar-link">Perfil </a>');
    }
    else{
        $('#sesion').append('<a href="iniciar_sesion.html" class="navbar-link">Iniciar Sesión </a>');
        $('#registro').append('<a href="registro.html" class="navbar-link" >Registrarse </a>');
    }
    /*obtener usuarios registrados hoy */
    let jugadores = 0;
    let titular=0;
    Users.forEach(usuario => {    
      if (jugadores==0 && titular==0) {
        $('.primera').append('<div id="primera-titular-1"><h4 class="titulares">Nuevos Jugadores!</h4></div>');
        jugadores++;
      }
      if (jugadores >= 1) {
        $('#primera-titular-1').append('<p><img class="imgRedonda" src="../assets/imgs/megaphone.svg"/> "'+usuario+'" se acaba unir hoy a DNTgames.</p>');
      }
      titular++;
    });
    //REVISAMO SI HUBO CAMBIOS EN JUGADORES HISTORICOS
    let pos;
    //console.log(jug_hist_actual.length);
    let jug = 0;
    for (let x = 0; x < jug_hist_actual.length; x++) {
      pos = x+1;
      if (jug_hist.length <= x ) {
        jug = jug +1;
      }
      else{
        if (jug_hist[x].username != jug_hist_actual[x].username) {
          jug = jug + 1;
        }
      }
      if (x==0 && jug >= 1) {
        $('.primera').append('<div id="primera-titular-0"><h4 class="titulares">Cambios en jugadores hístoricos!</h4></div>');
      }
      if (jug >= 1) {
        $('#primera-titular-0').append('<p><img class="imgRedonda" src="../assets/imgs/megaphone.svg"/>El usuario "'+jug_hist_actual[x].username+'" paso a la posición '+pos+'° en Jugadores Hístoricos</p>');
      }
    }
    //GUARDAMOS LOS JUGADORES ACTUALES
    jug_hist = jug_hist_actual.slice();
    localStorage.setItem('jug_hist_nov', JSON.stringify(jug_hist));
});

$("#sesion-cerrar").click(function(event){
    Users.forEach(element => {
        if (element.sesion === true) {
          element.sesion = false;
          //localStorage.setItem('usuarios', JSON.stringify(Users));
          return;
        }
      });
});