async function find_player(){
    var player = await fetch('https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/players/find', {
    method: 'POST', // or 'PUT'
    body: JSON.stringify({"username": JSON.parse(localStorage.getItem('user_sesion')).username}), // data can be `string` or {object}!
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(res => res.json())
  .then(function(response){
      console.log(response);
      return response;
    });

    if (player){
        return 1;
    }
    else{
        return 0;
    }
}

var User = localStorage.getItem('user_sesion');
if (localStorage){
    if (User !== null && User) {
        var user = JSON.parse(User);
        }
    else{
        var user = null;
      }
}
/*
var exists = find_player();

if (exists == 1){
    document.getElementById('a_juego').style.visibility = "visible";
}
else{
    document.getElementById('a_juego').style.visibility = "hidden";
}*/

console.log(user.partida);
if (user.partida){
    document.getElementById('a_juego').style.visibility = 'visible';
}
else {
    document.getElementById('a_juego').style.visibility = 'hidden';
}

$( document ).ready(function(){
    /*NAVBAR */
    if (user != null) {
        $('#sesion1').append('<a href="seleccion_partida.html" class="navbar-link">Jugar </a>');
       // $('h3').text(user.username)/*Aca abría que hacer  un click evento con este botoncito */
        //$('#sesion-cerrar').append('<a href="iniciar_sesion.html" class="navbar-link">Cerrar Sesión </a>');
        $('#perfil').append('<a href="perfil.html" class="navbar-link">Perfil </a>');
    }
    else{
        $('#sesion').append('<a href="iniciar_sesion.html" class="navbar-link">Iniciar Sesión </a>');
        $('#registro').append('<a href="registro.html" class="navbar-link" >Registrarse </a>');
    }
    /* FIN NAVBAR*/
    
})