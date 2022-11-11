var User = localStorage.getItem('user_sesion');
if (localStorage){
    if (User !== null && User) {
        var user = JSON.parse(User);
        }
    else{
        var user = null;
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
var agregados = [];

$(document).ready(async function(){
    //mostrar partidas publicas que fueron creadas hoy
    var partidas = await obtener_partidas("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/part_publicas/");
    let hora_actual = new Date()
    console.log(partidas.length);
    for (let x = 0; x < partidas.length; x++) {
        let hora = new Date(partidas[x].createdAt);
        let hours_part = parseInt(hora.getHours());
        let hours_actual = parseInt(hora_actual.getHours());
        
       
        if (partidas[x].id_part != user.username) {
            if (hora.getDate()==hora_actual.getDate() && hours_part+1>=hours_actual ){
                //console.log(hours_part, hours_actual);
                console.log(partidas);
                if(partidas[x].jug.length < partidas[x].n_jug ){
                $('div#anfitriones').append('<div class="p" >'+partidas[x].id_part +'</div>');
                $('div#numero-jugadores').append('<div class="p2">'+partidas[x].n_jug +'</div>');
                $('div#unirse').append('<div class="p2"><button class="boton_personal" id="buttons" value="'+partidas[x].id+'">entrar</button></div>');
                }
            }
        }
    }
    /*
    for (let index = 0; index < partidas.length; index++) {
        if (partidas[index].createdAt. ==){
            
        }
        
    }*/
    //fecha.getDate() : día de hoy



    //interval();
});



function obtener_partidas(url){
    const myHeader = {
        "Authorization": "Bearer "+user.token,
        "Content-type":"application/json"
        };
    return fetch(url,{method:"GET", headers:myHeader})
    .then(respuesta => { return respuesta.json() })
}


//-------------------------

$(function() {
    $(document).on('click', '#buttons',async function(event) {
       let id_part = this.value;
       //console.log(id_part);
       //console.log("Se presionó el Boton con Id :"+ id_part)
       //agregar el jugador(user_sesion) a la lista jug de la partida actual
       
        //ACÁ TENERMOS EL id_part QUE SE SELECIONÓ
    
        //obtenemos el n_jug de Partida seleccionada
        var partida_seleccionada = await Partida_select(id_part);

        //Pasamos el n_part 
        console.log(partida_seleccionada);

        //CREAMOS EL PLAYER que se unirá a la partida
        const player = await Crear_jugador(id_part, 2);
        //Actualizamos los jugadores de la partida
        partida_seleccionada.jug.push(player.username);

        //Actualizamos user_sesion para indicar que existe una partida
        user.partida = true;
        localStorage.setItem('user_sesion', JSON.stringify(user));

        //Actualizamos el mapa

        //Actualizamos los datos de la partida
        const url = "https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/part_publicas/update/"+id_part;
        const resp = await Actualizar_partida(url, partida_seleccionada);
        console.log(resp);
        //console.log(player.id);
        //console.log(player.id_jug);
        //console.log(player);
        //CREAMOS UN SEGUNDO PLAYER
        //console.log(player2.id_jug);
        localStorage.setItem('partida_actual', JSON.stringify(id_part));
        window.location.href = '../views/espera_partida.html';
     });
});

async function Partida_actualizada(url, partida){
    const part = await Actualizar_partida(url, partida);
    return part
}

function Actualizar_partida(url, partida){
    const myHeader = {
        "Authorization": "Bearer "+user.token,
        "Content-type":"application/json"
        };
    return fetch(url, {method:"PATCH", body:JSON.stringify(partida), headers:myHeader})
        .then(respuesta => { return respuesta.json() })
}



async function Partida_select(id_part){
    const part = await recibePartida("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/part_publicas/"+id_part);
    return part
}

function recibePartida(url){
    const myHeader = {
        "Authorization": "Bearer "+user.token,
        "Content-type":"application/json"
        };
    return fetch(url, {method:"GET", headers:myHeader})
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

   /*
   al seleccionar una partida
   debemos actualizar la lista jug de la aprtida seleccionada
   subir a local storage el id de la partida del jugador en cliente
   */
