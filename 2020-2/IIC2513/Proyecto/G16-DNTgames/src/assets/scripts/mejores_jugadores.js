//var Local = localStorage.getItem('usuarios');
var User = localStorage.getItem('user_sesion');
var jug_hist = [];

/* CARGAR DATOS */
if (localStorage){
  /*
  if (Local !== null && Local) {
    var Users = JSON.parse(Local);
    }
  else{
    var Users = [];
  }*/
  if (User !== null && User) {
    var user = JSON.parse(User);
    }
  else{
    var user = null;
  }
}

$( document ).ready(async function() {

    if (user) {
        $('#sesion1').append('<a href="seleccion_partida.html" class="navbar-link">Jugar </a>');
        /*Aca abría que hacer  un click evento con este botoncito */
        $('#sesion-cerrar').append('<a id="logout" class="navbar-link">Cerrar Sesión </a>');
        $('#perfil').append('<a href="perfil.html" class="navbar-link">Perfil </a>');
    }
    else{
        $('#sesion').append('<a href="iniciar_sesion.html" class="navbar-link">Iniciar Sesión </a>');
        $('#registro').append('<a href="registro.html" class="navbar-link" >Registrarse </a>');
    }
    /* FIN NAVBAR*/
    //obtenmos a los usuarios
    var Users = await Obtener_users("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/users");
    //var Users = [];
    /* BUSCAMOS A LOS 10 MEJORES JUGADORES*/
    let gan_netas_1;
    let gan_netas_2;
    let cambio;
    let j;
    for (let index = 1; index < Users.length; index++) {
        gan_netas_1 = Users[index].part_g - Users[index].part_p;
        gan_netas_2 = Users[index - 1].part_g - Users[index - 1].part_p;
        j = index;
        while (j>0 &&  gan_netas_1 > gan_netas_2) {
            cambio = Users[index];
            Users[index] = Users[index-1];
            Users[index-1] = cambio;
            j = j-1;
        }
    }
    //YA TENEMOS ORDENADOS USERS
    //PASAR DATOS
    for (let i = 0; i < Math.min(Users.length, 10); i++) {
        jug_hist[i] = Users[i];
    }
    //GUARDAMOS USUARIOS CON NUEVO ORDEN
    localStorage.setItem('usuarios', JSON.stringify(Users));
    //GUARDAMOS JUGADORES HISTORICOS
    localStorage.setItem('jug_historicos', JSON.stringify(jug_hist));
    // MOSTRAMOS JUGADORES
    let pos;
    for (let x = 0; x < jug_hist.length; x++) {
        pos = x +1;
        $('#N').append('<div class="j"> '+pos+') </div>');
        $('#U').append('<div class="j2"> '+jug_hist[x].username+' </div>');
        $('#P').append('<div class="j2">'+(jug_hist[x].part_g - jug_hist[x].part_p)+' </div>');
    }
});

function Obtener_users(url){
  return fetch(url)
  .then(respuesta => { return respuesta.json() })
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




$("#logout").click(recibeListado);