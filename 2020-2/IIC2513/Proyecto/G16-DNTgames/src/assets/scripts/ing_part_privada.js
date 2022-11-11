var User = localStorage.getItem('user_sesion');
var Priv = localStorage.getItem('part_privadas');
if (localStorage){
    if (User !== null && User) {
        var user = JSON.parse(User);
        }
    else{
        var user = null;
    }
    if (Priv !== null && Priv) {
        var privadas = JSON.parse(Priv);
        }
    else{
        var privadas = [];
    }
}
if (user !== null) {
    $('#sesion1').append('<a href="seleccion_partida.html" class="navbar-link">Jugar </a>');
    $('#sesion-cerrar').append('<a href="iniciar_sesion.html" class="navbar-link">Cerrar Sesión </a>');
    $('#perfil').append('<a href="perfil.html" class="navbar-link">Perfil </a>');
}
else{
    $('#sesion').append('<a href="iniciar_sesion.html" class="navbar-link">Iniciar Sesión </a>');
    $('#registro').append('<a href="registro.html" class="navbar-link" >Registrarse </a>');
}


$( "form" ).submit(function( event ) {
    let encontro = false;
    let partida = {};
    var jugadores = false;
    privadas.forEach(part => {
        if (part.id_part == $('input#id').val()) {
            encontro = true;
            partida = part;
            jugadores = part.jug.length;
        }
    });
    if (encontro) {
        //nose porque dice que jugadores es undefine???
        console.log(jugadores);
        console.log(partida.n_jug);
        if (partida.jug.length <= partida.n_jug) {
            let hora = new Date();
            if (hora.getDate() <= partida.dia_inicio && hora.getHours() <= partida.hora_inicio && hora.getMinutes() <= partida.minuto_inicio) {
                //agregamos al nuevo jugador a la partida_priv
                partida['jug'].push(user.username);
                //subimos los cambios
                localStorage.setItem('partida_actual', JSON.stringify(partida));
                //guardamos cambios en part_privadas
               localStorage.setItem('part_privadas', JSON.stringify(privadas));
                //Redireccionamos a espera.
                event.preventDefault();
                window.location.href = '../views/espera_partida.html';
            }
            else{
                $('div#mensaje').text('La partida ya comenzo').show();
            }
        }
        else{
            $('div#mensaje').text('Ya estan los jugadores maximo').show().fadeOut( 10000 );;
        }
    }
    else{
        $('div#mensaje').text('El id ingresado no es valido').show();
    }
});




$("#sesion-cerrar").click(function(event){
    if (user.sesion === true) {
      user.sesion = false;
      localStorage.setItem('usuarios', JSON.stringify(Users));
      localStorage.setItem('user_sesion', null);
      return;
    }
  });