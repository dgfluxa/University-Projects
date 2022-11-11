var User = localStorage.getItem('user_sesion');
if (localStorage){
    if (User !== null && User) {
        var user = JSON.parse(User);
        }
    else{
        var user = null;
      }
}

//-----FUNCIÓN CREAR Poblar MAPA
function poblar_lugares (mapa_lugares){
    /* Creamos bosques */
    for (let i=1; i <= 20; i++){
        var col = Math.floor(Math.random() * 25);
        var fila = Math.floor(Math.random() * 15);
        mapa_lugares[fila][col] = "B";}
    /* Creamos minas */
    for (let i=1; i <= 20; i++){
        var col = Math.floor(Math.random() * 25);
        var fila = Math.floor(Math.random() * 15);
        mapa_lugares[fila][col] = "M";}
    /* Creamos ruinas */
    for (let i=1; i <= 10; i++){
        var col = Math.floor(Math.random() * 25);
        var fila = Math.floor(Math.random() * 15);
        mapa_lugares[fila][col] = "R";}
    /* Creamos poblados */
    for (let i=1; i <= 10; i++){
        var col = Math.floor(Math.random() * 25);
        var fila = Math.floor(Math.random() * 15);
        mapa_lugares[fila][col] = "P";}
    /* Creamos Fortaleza */
    mapa_lugares[14][24] = "F";
    mapa_lugares[0][0] = "F";
    //la otra seria en [1][1]
};







$( document ).ready(function(){
    /*NAVBAR */
    if (user != null) {
        $('#sesion1').append('<a href="seleccion_partida.html" class="navbar-link">Jugar </a>');
        $('h3').text(user.username)/*Aca abría que hacer  un click evento con este botoncito */
        //$('#sesion-cerrar').append('<a href="iniciar_sesion.html" class="navbar-link">Cerrar Sesión </a>');
        $('#perfil').append('<a href="perfil.html" class="navbar-link">Perfil </a>');
    }
    else{
        $('#sesion').append('<a href="iniciar_sesion.html" class="navbar-link">Iniciar Sesión </a>');
        $('#registro').append('<a href="registro.html" class="navbar-link" >Registrarse </a>');
    }
    /* FIN NAVBAR*/
    var API = document.getElementById("API");
    //console.log(API);


    API.addEventListener("click", crear_partida_player_publica);

    
})


async function crear_partida_player_publica(){
    //VEMOS QUE MAPA SE ESCOGIO
    //CREAMOS MAPA
    var mapa_lugares = [];
    for (let i=1; i <= 15; i++){
        var fila = [];
        for (let j=1; j <= 25; j++){
            fila.push(0);
        }
        mapa_lugares.push(fila);
    }
    //llenamos aleatoriamente el mapa
    poblar_lugares(mapa_lugares);
    

    //TIEMPOS
    //obtenemos los datos de la partida
    var partida = {
        'n_part' : 1,
        'id_part' : user.username,
        'num_partidas': $('select.turnos-partida').val(),
        'mapa': mapa_lugares,
        'n_jug' : $('input.n-jugadores').val(),
        'jug': [user.username]
    };
    //creamos la partida
    const partida_creada = await enviaRequest("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/part_publicas/new", partida);
    //console.log(partida_creada);
    //--fin de crear partida
    //creameos el player
    const jugador = await Crear_jugador(partida_creada.id, 1);
    //console.log(jugador.id);
    console.log(jugador);
    if (jugador != undefined) {
        console.log(jugador.id_jug);
        $(location).attr('href', "../views/espera_partida.html");
    }
        //guardamos la partida
    localStorage.setItem('partida_actual', JSON.stringify(partida_creada.id));

    //Actualizamos user_sesion para indicar que existe una partida
    user.partida = true;
    localStorage.setItem('user_sesion', JSON.stringify(user));
    
}

function enviaRequest(url, datos){
    const myHeader = {
        "Authorization": "Bearer "+user.token,
        "Content-type":"application/json"
        };
    return fetch(url, {method:"POST",body:JSON.stringify(datos) ,headers:myHeader})
    .then(respuesta => { return respuesta.json() })
}

async function Crear_jugador(id, id_jug){
    const player = await recibePlayer("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/players/new", id, id_jug);
    return player;
}


//METODO POST PARA PLAYER (SE CREA UN PLAYER)
function recibePlayer(url, id, id_jug){
    const myHeader = {
        "Authorization": "Bearer "+user.token,
        "Content-type":"application/json"
        };
    const datos = {
        'username': user.username,
        'id_part': id,
        'id_jug': id_jug
    }
    return fetch(url, {method:"POST",body:JSON.stringify(datos) ,headers:myHeader})
    .then(respuesta => { return respuesta.json() })
}

//console.log($('input').val());