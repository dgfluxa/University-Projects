var User = localStorage.getItem('user_sesion');
let Partida = localStorage.getItem('partida_actual');
if (localStorage){
    if (User !== null && User) {
        var user = JSON.parse(User);
        }
    else{
        var user = null;
    }
    if (Partida !== null && Partida) {
        var id_partida = JSON.parse(Partida);
    }
    else{
        id_partida = null;
    }
}

$(document).ready(ejecutar);
    
async function ejecutar(){
    //mostramos jugadores
    if (id_partida !== null) {
        //buscamos a la partida con id id_partida
        var partida_actual = await Obtener_partida();
        const inicio_partida = new Date(partida_actual.createdAt)
        const hora_actual = new Date();
        const tiempo = 100 - (hora_actual.getSeconds() - inicio_partida.getSeconds());
        //console.log(partida_actual);
        for (let x = 0; x < partida_actual.n_jug; x++) {
            $('div.jugadores-listos').append('<div class="j" id="gamer'+x+'"></div>');
        }
        //mostramos el id de la partida
       // $('div.tiempo').append('<div class="jugador">ID Partida: <div class="j">'+partida.id_part+'</div></div>');
        $( "#ID" ).text( partida_actual.id ).show()
        localStorage.setItem('jugadores_actuales', JSON.stringify(partida_actual.jug));
        //mostramos el tiempo
        //$('div.tiempo').append('<div class="jugador" id="time_espera">Tiempo:</div>');
        console.log(tiempo)
        interval(tiempo);
    }
}

async function Obtener_partida(){
    const partida = await recibePartida("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/part_publicas/"+id_partida);
    return partida;
}

function recibePartida(url){
    const myHeader = {
        "Authorization": "Bearer "+user.token,
        "Content-type":"application/json"
        };
    return fetch(url, {method:"GET", headers:myHeader})
    .then(respuesta => { return respuesta.json() })
}

function interval(tiempo){
    t=tiempo;
    let Partida;
    let id;
    inter=setInterval(async function(){

        //se obtiene nuevamente la partida
        Partida = localStorage.getItem('jugadores_actuales');
        if (localStorage) {
            if (Partida !== null && Partida) {
                var jug_actuales = JSON.parse(Partida);
            }
            else{
                var jug_actuales = [];
            }
        }
        //ya tenemos partida
        document.getElementById("time_espera").innerHTML=t-- + 'seg';
        for (let x = 0; x< jug_actuales.length; x++) {
            id = "gamer"+x;
            document.getElementById(id).innerHTML= jug_actuales[x];
        }
        let numero = (jug_actuales.length);
        if (t==10) {
            var partida = await Obtener_partida();
            console.log(partida);
            for (let x = 0; x < partida.n_jug; x++) {
                $('div#gamer'+x).text(partida.jug[x]).show();
            }
            $( "#ID" ).text( partida.id ).show()
        }
        
        if(t==0 ){
            //aca deberías actualizar con PATCH las lista de jug y mapa con fortalezas
            window.location.href = '../views/juego.html';
        }
    },1000,"JavaScript");
}
