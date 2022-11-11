/*------------------- FUNCIONES --------------------*/

function casillas_moverse (mapa_visitados) { 
    for (let i=1; i <= 15; i++){
        for (let j=1; j <= 25; j++){
            if (mapa_visitados[i-1][j-1] == "E"){
                var mapa_moverse = [];
                for (i2=1; i2 <= 15; i2++){
                    var fila = [];
                    for (j2=1; j2 <= 25; j2++){
                        fila.push(0);
                    }
                    mapa_moverse.push(fila);
                }
                for (let n=0; n < 4; n++){
                    for (let m=0; m < 4; m++){
                        if (i+n <= 15 && i+n > 0){
                            if (j+m <= 25 && j+m > 0){
                                mapa_moverse[i+n-1][j+m-1] = 1;
                            }
                            if (j-m > 0 && j-m <= 25){
                                mapa_moverse[i+n-1][j-m-1] = 1;
                            }
                        }
                        if (i-n > 0 && i-n <= 15){
                            if (j+m <= 25 && j+m > 0){
                                mapa_moverse[i-n-1][j+m-1] = 1;
                            }
                            if (j-m > 0 && j-m <= 25){
                                mapa_moverse[i-n-1][j-m-1] = 1;
                            }
                        }
                        
                    }
                }
            }
            
        }
    }
    for (let i=0; i < 15; i++){
        for (let j=0; j < 25; j++){
            if (mapa_moverse[i][j] == 1) {
                var casilla = document.createElement("a");
                casilla.style.cursor = "pointer";
                casilla.className = "button";
                casilla.style.gridColumn = j+1;
                casilla.style.gridRow = i+1;
                casilla.onclick = function() {click_casilla(this);};
                document.getElementById("mapa").appendChild(casilla);
            }
        }
    }
};

function ocultar_mapa (mapa_visitados){
    var mapa_ocultos = [];
        for (i2=1; i2 <= 15; i2++){
            var fila = [];
            for (j2=1; j2 <= 25; j2++){
                fila.push("1");
            }
            mapa_ocultos.push(fila);
        }
    for (let i=1; i <= 15; i++){
        for (let j=1; j <= 25; j++){
            if (mapa_visitados[i-1][j-1] != 0){
                for (let n=0; n < 8; n++){
                    for (let m=0; m < 8; m++){
                        if (i+n <= 15 && i+n > 0){
                            if (j+m <= 25 && j+m > 0){
                                mapa_ocultos[i+n-1][j+m-1] = 0;
                            }
                            if (j-m > 0 && j-m <= 25){
                                mapa_ocultos[i+n-1][j-m-1] = 0;
                            }
                        }
                        if (i-n > 0 && i-n <= 15){
                            if (j+m <= 25 && j+m > 0){
                                mapa_ocultos[i-n-1][j+m-1] = 0;
                            }
                            if (j-m > 0 && j-m <= 25){
                                mapa_ocultos[i-n-1][j-m-1] = 0;
                            }
                        }
                    }
                }
            }
        }
    }
    for (let i=0; i < 15; i++){
        for (let j=0; j < 25; j++){
            if (mapa_ocultos[i][j] == 1) {
                var casilla = document.createElement("a");
                casilla.className = "desconocido";
                casilla.style.gridColumn = j+1;
                casilla.style.gridRow = i+1;
                casilla.style.zIndex = 5;
                document.getElementById("mapa").appendChild(casilla);
            }
        }
    }
};

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
};

function mostrar_lugares(mapa_lugares, mapa_visitados, num_jug){
    for (let i=1; i <= 15; i++){
        for (let j=1; j <= 25; j++){
            if (mapa_visitados[i-1][j-1] == "E"){
                var ejercito = document.createElement("DIV");
                ejercito.className = "lugar";
                ejercito.id = "div_ejercito"
                ejercito.style.gridColumn = j;
                ejercito.style.gridRow = i;
                ejercito.style.zIndex = 5;
                document.getElementById("mapa").appendChild(ejercito);
                if (num_jug == 1){
                    $('#div_ejercito').append('<img class="icono_ejercito" src="../assets/imgs/estrella.svg"/>');
                }
                else{
                    $('#div_ejercito').append('<img class="icono_ejercito2" src="../assets/imgs/estrella.svg"/>');
                }
            }
        }
    }
    for (let i=0; i < 15; i++){
        for (let j=0; j < 25; j++){
            if (mapa_lugares[i][j] != 0) {
                var lugar = document.createElement("DIV");
                lugar.className = "lugar";
                lugar.style.gridColumn = j+1;
                lugar.style.gridRow = i+1;
                var imagen = document.createElement("img")
                imagen.className = "icono_lugar";
                if (mapa_lugares[i][j] == "B"){
                    imagen.src = "../assets/imgs/bosque.svg";
                    imagen.id = "bosque";
                }
                else if (mapa_lugares[i][j] == "R"){
                    imagen.src = "../assets/imgs/ruinas.svg";
                    imagen.id = "ruinas";
                }
                else if (mapa_lugares[i][j] == "M"){
                    imagen.src = "../assets/imgs/mina.svg";
                    imagen.id = "mina";
                }
                else if (mapa_lugares[i][j] == "P"){
                    imagen.src = "../assets/imgs/casas.svg";
                    imagen.id = 'pueblo';
                }
                else if (mapa_lugares[i][j] == "PJ1"){
                    imagen.src = "../assets/imgs/casas.svg";
                    imagen.id = 'puebloJ1';
                }
                else if (mapa_lugares[i][j] == "PJ2"){
                    imagen.src = "../assets/imgs/casas.svg";
                    imagen.id = 'puebloJ2';
                }
                else if (mapa_lugares[i][j] == "PJ3"){
                    imagen.src = "../assets/imgs/casas.svg";
                    imagen.id = 'puebloJ3';
                }
                else if (mapa_lugares[i][j] == "PJ4"){
                    imagen.src = "../assets/imgs/casas.svg";
                    imagen.id = 'puebloJ4';
                }
                else {
                    imagen.src = "../assets/imgs/citadel.svg";
                    imagen.id = "fortaleza";
                }
                lugar.appendChild(imagen);
                document.getElementById("mapa").appendChild(lugar);
            }
        }
    }
};

function click_mover(){
    if (JSON.parse(localStorage.getItem("casillas")) != "1"){
        localStorage.setItem("casillas", JSON.stringify(1));
        var casillas = document.getElementsByClassName("button");
        for (let i=0; i<casillas.length; i++){
            casillas[i].style.visibility = "visible";
        }
    }
    else{
        localStorage.setItem("casillas", JSON.stringify(0));
        var casillas = document.getElementsByClassName("button");
        for (let i=0; i<casillas.length; i++){
            casillas[i].style.visibility = "hidden";
        }
    }
    return;
};

function click_casilla(casilla){
    var turno = JSON.parse(localStorage.getItem('turno'));
    var casillas = document.getElementsByClassName("button");
        for (let i=0; i<casillas.length; i++){
            casillas[i].style.backgroundColor = "blue";
        }
    casilla.style.backgroundColor = "red";
    var new_x = parseInt(casilla.style.gridColumn.split(" ", 1)[0]) - 1;
    var new_y = parseInt(casilla.style.gridRow.split(" ", 1)[0]) - 1;

    var turno = JSON.parse(localStorage.getItem('turno'));

    turno.jugada.x = new_x;
    turno.jugada.y = new_y;

    document.getElementById("mover").style.backgroundColor = 'red';

    var mapa_lugares = turno.mapa_lugares;
    var mapa_visitados = turno.jugador.mapa_visitados;

    var dict = {
        1: "PJ1",
        2: "PJ2",
        3: "PJ3",
        4: "PJ4",
    }

    if (mapa_lugares[new_y][new_x] != 0){
        
        if (mapa_lugares[new_y][new_x] == "P" || mapa_lugares[new_y][new_x] == "F" || mapa_lugares[new_y][new_x] == dict[turno.jugador.id_jug]){ //Arreglar para multijugdor

            var boton = document.getElementById("interactuar");
            if (boton) {
                boton.id = "interactuar_dis";
            }
            
            var boton = document.getElementById("comprar_guerrero_dis");
            if (boton && turno.jugador.dinero >= 80) {
                boton.id = "comprar_guerrero";
            }
            var boton = document.getElementById("comprar_doctor_dis");
            if (boton && turno.jugador.dinero >= 100) {
                boton.id = "comprar_doctor";
            }
            var boton = document.getElementById("comprar_obrero_dis");
            if (boton && turno.jugador.dinero >= 40) {
                boton.id = "comprar_obrero";
            }
            if (mapa_lugares[new_y][new_x] == "P"){
                var boton = document.getElementById("conquistar_dis");
                if (boton  && turno.jugador.dinero >= 300 && turno.jugador.madera >= 150) {
                    boton.id = "conquistar";
                }
            }
            else {
                var boton = document.getElementById("conquistar");
                if (boton) {
                    boton.id = "conquistar_dis";
                }
            }
        }
        else if (mapa_lugares[new_y][new_x] == "M" || mapa_lugares[new_y][new_x] == "B" || mapa_lugares[new_y][new_x] == "R"){
            var boton = document.getElementById("interactuar_dis");
            if (boton) {
                boton.id = "interactuar";
            }
            var boton = document.getElementById("conquistar");
            if (boton) {
                boton.id = "conquistar_dis";
            }
            var boton = document.getElementById("comprar_guerrero");
            if (boton) {
                boton.id = "comprar_guerrero_dis";
            }
            var boton = document.getElementById("comprar_doctor");
            if (boton) {
                boton.id = "comprar_doctor_dis";
            }
            var boton = document.getElementById("comprar_obrero");
            if (boton) {
                boton.id = "comprar_obrero_dis";
            }
        }
        else if (["PJ1", "PJ2", "PJ3", "PJ4"].includes(mapa_lugares[new_y][new_x]) && mapa_lugares[new_y][new_x] != dict[turno.jugador.id_jug] ){
            var boton = document.getElementById("interactuar_dis");
            if (boton) {
                boton.id = "interactuar";
            }
            var boton = document.getElementById("conquistar");
            if (boton) {
                boton.id = "conquistar_dis";
            }
            var boton = document.getElementById("comprar_guerrero");
            if (boton) {
                boton.id = "comprar_guerrero_dis";
            }
            var boton = document.getElementById("comprar_doctor");
            if (boton) {
                boton.id = "comprar_doctor_dis";
            }
            var boton = document.getElementById("comprar_obrero");
            if (boton) {
                boton.id = "comprar_obrero_dis";
            }
        }
        else{
            var boton = document.getElementById("interactuar");
            if (boton) {
                boton.id = "interactuar_dis";
            }
            var boton = document.getElementById("conquistar");
            if (boton) {
                boton.id = "conquistar_dis";
            }
            var boton = document.getElementById("comprar_guerrero");
            if (boton) {
                boton.id = "comprar_guerrero_dis";
            }
            var boton = document.getElementById("comprar_doctor");
            if (boton) {
                boton.id = "comprar_doctor_dis";
            }
            var boton = document.getElementById("comprar_obrero");
            if (boton) {
                boton.id = "comprar_obrero_dis";
            }
        }
    }
    else{
        var boton = document.getElementById("interactuar");
        if (boton) {
            boton.id = "interactuar_dis";
        }
        var boton = document.getElementById("conquistar");
        if (boton) {
            boton.id = "conquistar_dis";
        }
        var boton = document.getElementById("comprar_guerrero");
        if (boton) {
            boton.id = "comprar_guerrero_dis";
        }
        var boton = document.getElementById("comprar_doctor");
        if (boton) {
            boton.id = "comprar_doctor_dis";
        }
        var boton = document.getElementById("comprar_obrero");
        if (boton) {
            boton.id = "comprar_obrero_dis";
        }
        
    }
    localStorage.setItem('turno', JSON.stringify(turno));
};

function click_curar(boton){
    var turno = JSON.parse(localStorage.getItem('turno'));
    turno.jugada.curar = 1;
    localStorage.setItem('turno', JSON.stringify(turno));
    boton.style.backgroundColor = 'red';
};

function click_interactuar(boton){
    var turno = JSON.parse(localStorage.getItem('turno'));
    turno.jugada.interactuar = 1;
    localStorage.setItem('turno', JSON.stringify(turno));
    boton.style.backgroundColor = 'red';
};

function click_conquistar(boton){
    var turno = JSON.parse(localStorage.getItem('turno'));
    if (turno.jugada.conquistar == 0 && turno.jugador.dinero >=300 && turno.jugador.madera >= 150){
        turno.jugada.conquistar = 1;
        turno.jugador.dinero -= 300;
        turno.jugador.madera -= 150;
        turno.jugador.poblados += 1;
        localStorage.setItem('turno', JSON.stringify(turno));
        actualizar();
        boton.style.backgroundColor = 'red';
    }
    else{
        var boton = document.getElementById("conquistar");
        if (boton) {
            boton.id = "conquistar_dis";
        }
    }
    
};

function comprar_guerrero(){
    var turno = JSON.parse(localStorage.getItem('turno'));
    turno.jugador.guerreros += 1;
    turno.jugador.dinero -= 80;
    turno.jugador.salud += 300;
    turno.jugador.ataque += 300;
    turno.jugador.defensa += 200;
    turno.jugador.vida_actual += 300;
    turno.jugador.vida_max += 300;
    localStorage.setItem('turno', JSON.stringify(turno));
    actualizar();

    if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "P"){
        var boton = document.getElementById("conquistar");
        if (boton  && (turno.jugador.dinero < 300 || turno.jugador.madera < 150)) {
            boton.id = "conquistar_dis";
        }
    }


};

function comprar_doctor(){
    var turno = JSON.parse(localStorage.getItem('turno'));
    turno.jugador.doctores += 1;
    turno.jugador.dinero -= 100;
    turno.jugador.salud += 200;
    turno.jugador.ataque += 50;
    turno.jugador.defensa += 100;
    turno.jugador.vida_actual += 200;
    turno.jugador.vida_max += 200;
    localStorage.setItem('turno', JSON.stringify(turno));
    actualizar();

    if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "P"){
        var boton = document.getElementById("conquistar");
        if (boton  && (turno.jugador.dinero < 300 || turno.jugador.madera < 150)) {
            boton.id = "conquistar_dis";
        }
    }
};

function comprar_obrero(){
    var turno = JSON.parse(localStorage.getItem('turno'));
    turno.jugador.obreros += 1;
    turno.jugador.dinero -= 40;
    turno.jugador.salud += 100;
    turno.jugador.ataque += 20;
    turno.jugador.defensa += 30;
    turno.jugador.vida_actual += 100;
    turno.jugador.vida_max += 100;
    localStorage.setItem('turno', JSON.stringify(turno));
    actualizar();

    if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "P"){
        var boton = document.getElementById("conquistar");
        if (boton  && (turno.jugador.dinero < 300 || turno.jugador.madera < 150)) {
            boton.id = "conquistar_dis";
        }
    }
};
/* Rescatado de https://stackoverflow.com/questions/625920/jquery-popup-bubble-tooltip?rq=1 */
function createTooltip(event){          
    $('<div class="tooltip"></div>').appendTo('body');
    positionTooltip(event);        
};

function hideTooltip(){
    $('.tooltip').remove();
};

function positionTooltip(event){
    var tPosX = event.pageX -20;
    var tPosY = event.pageY - 50;
    $('div.tooltip').css({'top': tPosY, 'left': tPosX});
};
/* Termina lo rescatado */

function actualizar(){
    var turno = JSON.parse(localStorage.getItem('turno'));
    document.getElementById("num_madera").textContent = turno.jugador.madera;
    document.getElementById("num_dinero").textContent = turno.jugador.dinero;
    document.getElementById("num_vida").textContent = turno.jugador.vida_actual + '/' + turno.jugador.vida_max;
    document.getElementById("porc_vida").textContent = Math.round(turno.jugador.vida_actual * 100 /turno.jugador.vida_max);
    document.getElementById("vida_actual").style.width = (Math.round(turno.jugador.vida_actual * 100 /turno.jugador.vida_max)).toString() + "%";
    document.getElementById("num_poblados").textContent = turno.jugador.poblados;
    document.getElementById("porc_poblados").textContent = Math.round(turno.jugador.poblados * 100 /10);
    document.getElementById("pob_actual").style.width = (Math.round(turno.jugador.poblados * 100 /10)).toString() + "%";
    document.getElementById("num_guerreros").textContent = turno.jugador.guerreros;
    document.getElementById("num_doctores").textContent = turno.jugador.doctores;
    document.getElementById("num_obreros").textContent = turno.jugador.obreros;
    document.getElementById("num_ataque").textContent = turno.jugador.ataque;
    document.getElementById("num_salud").textContent = turno.jugador.salud;
    document.getElementById("num_defensa").textContent = turno.jugador.defensa;
    document.getElementById("turnos").textContent = turno.turnos_partida;

    var boton = document.getElementById("conquistar");
    if (boton && (turno.jugador.dinero < 100 || turno.jugador.madera < 50)) {
        boton.id = "conquistar_dis";
    }
    var boton = document.getElementById("comprar_guerrero");
    if (boton && turno.jugador.dinero < 80) {
        boton.id = "comprar_guerrero_dis";
    }
    var boton = document.getElementById("comprar_doctor");
    if (boton && turno.jugador.dinero < 100) {
        boton.id = "comprar_doctor_dis";
    }
    var boton = document.getElementById("comprar_obrero");
    if (boton && turno.jugador.dinero < 40) {
        boton.id = "comprar_obrero_dis";
    }
    var boton = document.getElementById("mover");
    if (boton && turno.jugador.vida_actual == 0) {
        boton.id = "mover_dis";
    }
};

function click_terminar(){
    var turno = JSON.parse(localStorage.getItem('turno'));
    localStorage.setItem('turno', JSON.stringify(turno));
    document.getElementById("boton_terminar").style.visibility = 'hidden';
    document.getElementById("boton_simular").style.visibility = 'visible';
    document.getElementById("boton_modificar").style.visibility = 'visible';
    document.getElementById("columna_der").id = 'columna_der_dis';
    document.getElementById("mapa").id = 'mapa_dis';
    document.getElementById("wrapper").id = 'wrapper_dis';

    var dict = {
        1: "PJ1",
        2: "PJ2",
        3: "PJ3",
        4: "PJ4",
    }

    //Agregamos numero de turno
    var texto_turno = document.createElement("p");
    texto_turno.textContent = 'Turno'; // + turno.jugada.numero;
    document.getElementById("cont_resumen").appendChild(texto_turno);

    //Agregamos lugar a moverse
    if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == 0){
        var nombre_lugar = "Planicie";
    }
    else if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "F"){
        var nombre_lugar = "Fortaleza";
    }
    else if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "M"){
        var nombre_lugar = "Mina";
    }
    else if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "B"){
        var nombre_lugar = "Bosque";
    }
    else if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "R"){
        var nombre_lugar = "Ruinas";
    }
    else{
        var nombre_lugar = "Poblado";

    }
    var texto_lugar = document.createElement("p");
    texto_lugar.textContent = 'Lugar Objetivo: ' + nombre_lugar;
    document.getElementById("cont_resumen").appendChild(texto_lugar);

    //Agregar si se conquista
    if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "P"){
        if (turno.jugada.conquistar == 1){
            var realizar = "Sí"
        }
        else{
            var realizar = "No"
        }
        
        var texto_accion = document.createElement("li");
        texto_accion.textContent = 'Conquistar: ' + realizar;
        document.getElementById("lista_resumen").appendChild(texto_accion);
    }

    //Agregar si se interactúa
    if (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "M" || turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "B" || turno.mapa_lugares[turno.jugada.y][turno.jugada.x] == "R" || (turno.mapa_lugares[turno.jugada.y][turno.jugada.x] in ["PJ1", "PJ2", "PJ3", "PJ4"] && turno.mapa_lugares[turno.jugada.y][turno.jugada.x] != dict[turno.jugador.id_jug])){
        if (turno.jugada.interactuar == 1){
            var realizar = "Sí"
        }
        else{
            var realizar = "No"
        }
        
        var texto_accion = document.createElement("li");
        texto_accion.textContent = 'Interactuar: ' + realizar;
        document.getElementById("lista_resumen").appendChild(texto_accion);
    }

    //Agregar si se cura
    if (turno.jugada.curar == 1){
        var realizar = "Sí"
    }
    else{
        var realizar = "No"
    }
    
    var texto_accion = document.createElement("li");
    texto_accion.textContent = 'Curar: ' + realizar;
    document.getElementById("lista_resumen").appendChild(texto_accion);

    //Agregar si se compran unidades
    //Guerreros
    var turno_p = JSON.parse(localStorage.getItem('turno_pasado'));
    if (turno.jugador.guerreros > turno_p.jugador.guerreros){
        var texto_comprar = document.createElement("li");
        texto_comprar.textContent = 'Comprar Guerreros: ' + (turno.jugador.guerreros - turno_p.jugador.guerreros);
        document.getElementById("lista_resumen").appendChild(texto_comprar);
    }
    //Doctores
    if (turno.jugador.doctores > turno_p.jugador.doctores){
        var texto_comprar = document.createElement("li");
        texto_comprar.textContent = 'Comprar Doctores: ' + (turno.jugador.doctores - turno_p.jugador.doctores);
        document.getElementById("lista_resumen").appendChild(texto_comprar);
    }
    //Obreros
    if (turno.jugador.obreros > turno_p.jugador.obreros){
        var texto_comprar = document.createElement("li");
        texto_comprar.textContent = 'Comprar Obreros: ' + (turno.jugador.obreros - turno_p.jugador.obreros);
        document.getElementById("lista_resumen").appendChild(texto_comprar);
    }

    document.getElementById("mensaje_resumen").style.visibility = 'visible';
    
    console.log(JSON.stringify(turno));
};

function click_modificar(){
    var turno = JSON.parse(localStorage.getItem('turno_pasado'));
    document.getElementById("boton_simular").style.visibility = 'hidden';
    document.getElementById("boton_modificar").style.visibility = 'hidden';
    document.getElementById("boton_terminar").style.visibility = 'visible';
    document.getElementById("columna_der_dis").id = 'columna_der';
    document.getElementById("mapa_dis").id = 'mapa';
    localStorage.setItem("casillas", JSON.stringify(0));

    /* Escondemos casillas de movimiento */
    var casillas = document.getElementsByClassName("button");
    for (let i=0; i<casillas.length; i++){
        casillas[i].style.backgroundColor = "blue";
        casillas[i].style.visibility = "hidden";
    }
    localStorage.setItem('turno', JSON.stringify(turno));
    actualizar();
};

async function click_simular(){
    var turno_p = JSON.parse(localStorage.getItem('turno_pasado'));
    var turno_orig = JSON.parse(localStorage.getItem('turno'));
    var turno = JSON.parse(localStorage.getItem('turno'));
    //var respuesta = JSON.parse(generar_respuesta(turno));
    //var respuesta = JSON.parse(localStorage.getItem('respuesta'));

    var url = 'https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/moves/process';

   /* var respuesta = fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(turno), // data can be `string` or {object}!
        headers: {
            'Content-Type': 'application/json'
          },
    });

    console.log(respuesta);*/

    var respuesta = await fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(turno), // data can be `string` or {object}!
        headers:{
          'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(function(response){
          console.log(response);
          return response;
    });
    

    var dict = {
        1: "PJ1",
        2: "PJ2",
        3: "PJ3",
        4: "PJ4"
    };

    var dict2 = {
        "PJ1": 1,
        "PJ2": 2,
        "PJ3": 3,
        "PJ4": 4
    };

    var lista = ["PJ1", "PJ2", "PJ3", "PJ4"];
    
    turno.jugador.mapa_visitados = respuesta.jugador.mapa_visitados;
    turno.jugador = respuesta.jugador;
    turno.jugada.numero = respuesta.jugada.numero;
    turno.mapa_lugares = respuesta.mapa_lugares;
    turno.jugada.conquistar = 0;
    turno.jugada.curar = 0;
    turno.jugada.interactuar = 0;
    var intento_x = turno.jugada.x;
    var intento_y = turno.jugada.y;
    turno.jugada.x = respuesta.jugada.x;
    turno.jugada.y = respuesta.jugada.y;
    turno.turnos_partida = respuesta.turnos_partida;

    
    localStorage.setItem('turno_pasado', JSON.stringify(turno));
    localStorage.setItem('turno', JSON.stringify(turno));

    //Poblar mensaje de resultados

    //Agregamos numero de turno
    var texto_turno = document.createElement("p");
    texto_turno.textContent = ' Resultados Turno'; //+ (respuesta.jugada.numero - 1);
    document.getElementById("cont_resultado").appendChild(texto_turno);

    //Agregamos si muere
    if (respuesta.muere == 1){
    var texto = document.createElement("p");
    texto.textContent = 'HAZ MUERTO';
    texto.style.fontSize = '3vh';
    texto.style.fontWeight = 'bold';
    texto.style.color = 'red';
    document.getElementById("cont_resultado").appendChild(texto);
    }

    //Agregamos lugar a moverse
    if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == 0){
        var nombre_lugar = "Planicie";
    }
    else if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "F"){
        var nombre_lugar = "Fortaleza";
    }
    else if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "M"){
        var nombre_lugar = "Mina";
    }
    else if (respuesta.mapa_lugares[respuesta.jugada.y][turno.jugada.x] == "B"){
        var nombre_lugar = "Bosque";
    }
    else if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "R"){
        var nombre_lugar = "Ruinas";
    }
    else{
        var nombre_lugar = "Poblado";
    }
    var texto_lugar = document.createElement("p");
    texto_lugar.textContent = 'Lugar Resultante: ' + nombre_lugar;
    document.getElementById("cont_resultado").appendChild(texto_lugar);


    //Agregamos si conquista con exito
    if (respuesta.jugada.exito_conquistar == 1){
        var texto = document.createElement("li");
        texto.textContent = 'Poblado conquistado con éxito';
        document.getElementById("lista_resultado").appendChild(texto);
        
    }

    //Agregamos si se recupera vida
    if(respuesta.jugador.vida_actual > turno_orig.jugador.vida_actual){
        var texto = document.createElement("li");
        texto.textContent = 'Tu vida ha aumentado en '+ (respuesta.jugador.vida_actual - turno_orig.jugador.vida_actual) + ' puntos de vida';
        document.getElementById("lista_resultado").appendChild(texto);
    }

    //Agregamos si interactua con exito
    if (respuesta.mapa_lugares[intento_y][intento_x] == "M"){
        if (respuesta.jugada.exito_interactuar == 1){
            var texto = document.createElement("li");
            texto.textContent = 'Recolectaste '+ (25 * respuesta.jugador.obreros) + ' monedas';
            document.getElementById("lista_resultado").appendChild(texto);
        }
        else if (respuesta.jugada.exito_interactuar == 0){
            var texto = document.createElement("li");
            texto.textContent = '¡Peligro! La mina no era segura, perdiste ' + (turno_orig.jugador.vida_actual - respuesta.jugador.vida_actual) + ' puntos de vida';
            document.getElementById("lista_resultado").appendChild(texto);
        }
    }
    else if (respuesta.mapa_lugares[intento_y][intento_x] == "B"){
        if (respuesta.jugada.exito_interactuar == 1){
            var texto = document.createElement("li");
            texto.textContent = 'Recolectaste '+ (20 * respuesta.jugador.obreros) + ' kg de madera';
            document.getElementById("lista_resultado").appendChild(texto);
        }
        else if (respuesta.jugada.exito_interactuar == 0){
            var texto = document.createElement("li");
            texto.textContent = '¡Peligro! Te encontraste con animales salvajes en el bosque, perdiste ' + (turno_orig.jugador.vida_actual - respuesta.jugador.vida_actual) + ' puntos de vida';
            document.getElementById("lista_resultado").appendChild(texto);
        }
    }
    else if (respuesta.mapa_lugares[intento_y][intento_x] == "R"){
        if (respuesta.jugada.exito_interactuar == 1){
            var dinero = document.createElement("li");
            var madera = document.createElement("li");
            var accesorio = document.createElement("li");
            var bandidos = document.createElement("li");
            if (turno_orig.jugador.vida_actual > respuesta.jugador.vida_actual){
                bandidos.textContent = '¡Peligro! Te enfrentaste a bandidos y triunfaste. En el enfrentamiento perdiste ' + (Math.max(0, turno_orig.jugador.vida_actual - respuesta.jugador.vida_actual)) + ' puntos de vida';
                document.getElementById("lista_resultado").appendChild(bandidos);
            }
            dinero.textContent = 'Encontraste '+ (respuesta.jugador.dinero - turno_orig.jugador.dinero) + ' monedas';
            document.getElementById("lista_resultado").appendChild(dinero);
            madera.textContent = 'Encontraste '+ (respuesta.jugador.madera - turno_orig.jugador.madera) + ' kg de madera';
            document.getElementById("lista_resultado").appendChild(madera);
            console.log("Acc turno orig: %s", JSON.stringify(turno_orig.jugador.accesorios));
            console.log("Acc respuesta: %s", JSON.stringify(respuesta.jugador.accesorios));
            if (turno_orig.jugador.accesorios.length != respuesta.jugador.accesorios.length){
                accesorio.textContent = 'Encontraste el accesorio "'+ respuesta.jugador.accesorios[respuesta.jugador.accesorios.length - 1] + '"'; 
                document.getElementById("lista_resultado").appendChild(accesorio);
            }
            
        }
        else if (respuesta.jugada.exito_interactuar == 0){
            var texto = document.createElement("li");
            texto.textContent = '¡Peligro! Te encontraste con bandidos y saliste derrotado, perdiste ' + (turno_orig.jugador.vida_actual - respuesta.jugador.vida_actual) + ' puntos de vida';
            document.getElementById("lista_resultado").appendChild(texto);
        }
    }
    else if (lista.includes(turno_orig.mapa_lugares[intento_y][intento_x])){

        var vida = document.createElement("li");
        
        if (respuesta.mapa_lugares[intento_y][intento_x] == dict[respuesta.jugador.id_jug]){
            var texto = document.createElement("li");
            texto.textContent = 'Haz logrado conquistar el poblado del otro jugador con éxito';
            document.getElementById("lista_resultado").appendChild(texto);
        }
        else{
            var texto = document.createElement("li");
            texto.textContent = '¡Oh no! Haz sido derrotado al invadir el poblado del otro jugador';
            document.getElementById("lista_resultado").appendChild(texto);
        }
        if (turno_orig.jugador.vida_actual > respuesta.jugador.vida_actual){
            vida.textContent = 'En el enfrentamiento perdiste ' + (Math.max(0, turno_orig.jugador.vida_actual - respuesta.jugador.vida_actual)) + ' puntos de vida';
            document.getElementById("lista_resultado").appendChild(vida);
        }

    }

    //Agregar si se compran unidades
    //Guerreros
    if (respuesta.jugador.guerreros > turno_p.jugador.guerreros){
        var texto_comprar = document.createElement("li");
        texto_comprar.textContent = 'Compraste ' + (respuesta.jugador.guerreros - turno_p.jugador.guerreros) + ' Guerrero(s)';
        document.getElementById("lista_resultado").appendChild(texto_comprar);
    }
    //Doctores
    if (respuesta.jugador.doctores > turno_p.jugador.doctores){
        var texto_comprar = document.createElement("li");
        texto_comprar.textContent = 'Compraste ' + (respuesta.jugador.doctores - turno_p.jugador.doctores) + ' Doctore(s)';
        document.getElementById("lista_resultado").appendChild(texto_comprar);
    }
    //Obreros
    if (respuesta.jugador.obreros > turno_p.jugador.obreros){
        var texto_comprar = document.createElement("li");
        texto_comprar.textContent = 'Compraste ' + (respuesta.jugador.obreros - turno_p.jugador.obreros) + ' Obrero(s)';
        document.getElementById("lista_resultado").appendChild(texto_comprar);
    }


    
    document.getElementById("wrapper").id = 'wrapper_dis';
    document.getElementById("mensaje_resultado").style.visibility = 'visible';

};

function generar_respuesta(turno){

    var respuesta = {
        'jugador': {
            'username': JSON.parse(localStorage.getItem('user_sesion')),
            'id_jug': id_jug,
            'guerreros': 0,
            'doctores': 0,
            'obreros': 0,
            'dinero': 300,
            'madera': 25,
            'accesorios': [],
            'poblados': 0,
            'mapa_visitados': turno.jugador.mapa_visitados,
            'vida_actual': 300,
            'vida_max': 300,
            'salud': 0,
            'ataque': 0,
            'defensa': 0
        },
        'jugada':{
            'numero': 1,
            'x': 24,
            'y': 14,
            'exito_interactuar': null,
            'exito_conquistar': null,
        },
        'mapa_lugares': turno.mapa_lugares,
        'id_partida': turno.id_partida,
        'turnos_partida': turno.turnos_partida,
        'muere': 0
    };

    respuesta.jugador = turno.jugador;
    respuesta.jugada.numero = turno.jugada.numero + 1;
    respuesta.jugada.x = turno.jugada.x;
    respuesta.jugada.y = turno.jugada.y;

    /*Si se encuentra en la fortaleza se le cura vida automáticamente */
    if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "F"){
        respuesta.jugador.vida_actual = Math.min(respuesta.jugador.vida_max, respuesta.jugador.vida_actual + 1500);
    }

    /* Actualizamos el mapa de sitios visitados y la posición del ejército del jugador */
    for (let i=1; i <= 15; i++){
        for (let j=1; j <= 25; j++){
            if (respuesta.jugador.mapa_visitados[i-1][j-1] == "E"){
                respuesta.jugador.mapa_visitados[i-1][j-1] = "V";
            }
        }
    }
    respuesta.jugador.mapa_visitados[turno.jugada.y][turno.jugada.x] = "E";

    /* Vemos si se desea curar */
    if (turno.jugada.curar == 1){
        respuesta.jugador.vida_actual = Math.min(respuesta.jugador.vida_max, respuesta.jugador.vida_actual + (100 * respuesta.jugador.doctores));
    }

    /* Vemos si se desea conquistar */
    if (turno.jugada.conquistar == 1){
        respuesta.mapa_lugares[turno.jugada.y][turno.jugada.x] = "PJ1";  
        respuesta.jugada.exito_conquistar = 1;
    }
    
    /* Vemos si se desea interactuar */
    if (turno.jugada.interactuar == 1){
        
        var numero = Math.floor(Math.random() * 100) + 1;
        if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "B"){
            if (numero > 25){
                respuesta.jugador.madera += 20 * respuesta.jugador.obreros;
                respuesta.jugada.exito_interactuar = 1;
            }
            else{
                var descuento = Math.floor(Math.random() * respuesta.jugador.salud/2) + respuesta.jugador.salud/5;
                respuesta.jugador.vida_actual = Math.max(respuesta.jugador.vida_actual - descuento, 0)
                respuesta.jugada.exito_interactuar = 0;
            }
        }
        else if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "M"){
            if (numero > 15){
                respuesta.jugador.dinero += 25 * respuesta.jugador.obreros;
                respuesta.jugada.exito_interactuar = 1;
            }
            else{
                var descuento = Math.floor(Math.random() * respuesta.jugador.salud/4 * 3) + respuesta.jugador.salud/4;
                respuesta.jugador.vida_actual = Math.max(respuesta.jugador.vida_actual - descuento, 0)
                respuesta.jugada.exito_interactuar = 0;
            }
        }
        else if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "R"){
        }
    }

    /*Vemos si ha muerto */
    if (respuesta.jugador.vida_actual == 0){
        respuesta.muere = 1;
        respuesta.jugador.mapa_visitados[respuesta.jugada.y][respuesta.jugada.x] = "V";
        respuesta.jugada.x = 24;
        respuesta.jugada.y = 14;
        respuesta.jugador.mapa_visitados[respuesta.jugada.y][respuesta.jugada.x] = "E";
    }

    return JSON.stringify(respuesta);
};

function cerrar_resumen(){
    document.getElementById("mensaje_resumen").style.visibility = 'hidden';
    document.getElementById("wrapper_dis").id = 'wrapper';
}

function cerrar_resultado(){
    document.getElementById("mensaje_resultado").style.visibility = 'hidden';
    document.getElementById("wrapper_dis").id = 'wrapper';
}

async function mostrar_fin(){
    document.getElementById("wrapper").id = 'wrapper_dis';

    var winner = await fetch('https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/moves/winner', {
    method: 'POST', // or 'PUT'
    body: JSON.stringify({"part_id": JSON.parse(localStorage.getItem('turno')).id_partida}),
    headers:{
      'Content-Type': 'application/json'
    }
    }).then(res => res.json())
    .catch(error => console.error('Error:', error))
    .then(function(response){
      console.log(response);
      return response;
    });


    var texto_ganador = document.createElement("p");
    texto_ganador.textContent = 'Ganador: ' + winner.username;
    document.getElementById("cont_fin").appendChild(texto_ganador);

    var texto_pob = document.createElement("p");
    texto_pob.textContent = 'Poblados Conquistados: ' + winner.poblados;
    document.getElementById("cont_fin").appendChild(texto_pob);


    
    document.getElementById("mensaje_fin").style.visibility = 'visible';
}

async function cerrar_fin(){
    await fetch('https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/moves/end', {
    method: 'POST', // or 'PUT'
    body: JSON.stringify({"username": JSON.parse(localStorage.getItem('user_sesion')).username}),
    headers:{
      'Content-Type': 'application/json'
    }
    }).then(res => res.json())
    .catch(error => console.error('Error:', error))
    .then(function(response){
      console.log(response);
      return response;
    });

    //Actualizamos user_sesion para indicar que no existe una partida
    var user = JSON.parse(localStorage.getItem('user_sesion'));
    user.partida = false;
    localStorage.setItem('user_sesion', JSON.stringify(user));
    localStorage.setItem("partida_iniciada", JSON.stringify(false));
    window.location.href = "../../index.html";


}

async function obtener_turno(){
    var turno = await fetch('https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/moves/start', {
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

    return turno;
}

async function check_player(){
    var check = await fetch('https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/moves/check_player', {
        method: 'POST', // or 'PUT'
        body: JSON.stringify({"username": JSON.parse(localStorage.getItem('user_sesion')).username}),
        headers:{
          'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(function(response){
          console.log(response);
          return response;
    });

    return check;
}

async function initiate(document){
    var turno = await obtener_turno();

    // Si se terminó la partida, mostrar resultados
    if (turno.turnos_partida <= 0){
        await mostrar_fin();
    }
    else{
        // Obtener si le toca a ese jugador de BDD
        var check = await check_player();
        
        
        // Si no le corresponde a su turno, redireccionar a error
        if (check.correct == 0){
            window.location.href = "../views/error_turno.html";
        }
    }
    localStorage.setItem('turno', JSON.stringify(turno));
    localStorage.setItem('turno_pasado', JSON.stringify(turno));
    localStorage.setItem('respuesta', JSON.stringify(turno));
    localStorage.setItem("partida_iniciada", JSON.stringify(true));
    
    /* Se revisa si ya se comenzó la partida para recuperar mapas o si no crear nuevos 
    if (JSON.parse(localStorage.getItem("partida_iniciada")) != null){
        var turno = JSON.parse(localStorage.getItem('turno'));
        var mapa_lugares = turno.mapa_lugares;
        var mapa_visitados = turno.jugador.mapa_visitados;
    }
    else {
        var mapa_lugares = [];
        for (let i=1; i <= 15; i++){
            var fila = [];
            for (let j=1; j <= 25; j++){
                fila.push(0);
            }
            mapa_lugares.push(fila);
        }
        poblar_lugares(mapa_lugares);
        localStorage.setItem('mapa_lugares', JSON.stringify(mapa_lugares));
        var mapa_visitados = [];
        for (let i=1; i <= 15; i++){
            var fila = [];
            for (let j=1; j <= 25; j++){
                fila.push(0);
            }
            mapa_visitados.push(fila);
        }
        mapa_visitados[14][24] = "E";
        localStorage.setItem("partida_iniciada", JSON.stringify(true));
    
        var id_jug = "J1"; //Cambiar al habilitar multijugador
        var id_partida = 1; //Cambiar al habilitar multijugador
        var turnos_partida = 10; //Cambiar futuro
    
        var turno = {
            'jugador': {
                'username': JSON.parse(localStorage.getItem('user_sesion')).username,
                'id_jug': id_jug,
                'guerreros': 0,
                'doctores': 0,
                'obreros': 0,
                'dinero': 300,
                'madera': 25,
                'accesorios': [],
                'poblados': 0,
                'mapa_visitados': mapa_visitados,
                'vida_actual': 300,
                'vida_max': 300,
                'salud': 0,
                'ataque': 0,
                'defensa': 0
            },
            'jugada':{
                'numero': 1,
                'x': 24,
                'y': 14,
                'interactuar': 0,
                'curar': 0,
                'conquistar': 0,
            },
            'mapa_lugares': mapa_lugares,
            'id_partida': id_partida,
            'turnos_partida': turnos_partida
        };
    
        
    
        localStorage.setItem('turno', JSON.stringify(turno));
        localStorage.setItem('turno_pasado', JSON.stringify(turno));
        localStorage.setItem('respuesta', JSON.stringify(turno));
    }*/
    
    /* Nombre de usuario */
    //document.getElementById('text_username').textContent = turno.jugador.username;

    var mapa_lugares = turno.mapa_lugares;
    var mapa_visitados = turno.jugador.mapa_visitados;
    
    /*Se muestra el mapa */
    mostrar_lugares(mapa_lugares, mapa_visitados, turno.jugador.id_jug);
    ocultar_mapa(mapa_visitados);
    casillas_moverse(mapa_visitados);
    actualizar();
    localStorage.setItem("casillas", JSON.stringify(0));
    
    /* Se habilita la compra de unidades antes de realizar un movimiento cuando se comienza desde una fortaleza o poblado*/
    if (mapa_lugares[turno.jugada.y][turno.jugada.x] == "F" || mapa_lugares[turno.jugada.y][turno.jugada.x] == "P"){
        var boton = document.getElementById("comprar_guerrero_dis");
        if (boton) {
            boton.id = "comprar_guerrero";
        }
        var boton = document.getElementById("comprar_doctor_dis");
        if (boton) {
            boton.id = "comprar_doctor";
        }
        var boton = document.getElementById("comprar_obrero_dis");
        if (boton) {
            boton.id = "comprar_obrero";
        }
    }
}
/*------------------- PROGRAMA --------------------*/

// Obtener valores de BDD


initiate(document);

var turno = JSON.parse(localStorage.getItem('turno'));
document.getElementById('text_username').textContent = turno.jugador.username;



/*-------------------------------------------------------*/

$(".boton_abandonar").click(function(event){
    localStorage.setItem("partida_iniciada", JSON.stringify(null));
    localStorage.setItem("casillas", JSON.stringify(0));
    return;
});



$('.icono_lugar').mouseover(function(event) {
    createTooltip(event); 
    if (this.id == "mina"){
        $(".tooltip").text("Mina");
    }  
    else if (this.id == "bosque"){
        $(".tooltip").text("Bosque");
    }   
    else if (this.id == "ruinas"){
        $(".tooltip").text("Ruinas");
    }
    else if (this.id == "pueblo"){
        $(".tooltip").text("Poblado");
    }
    else if (this.id == "puebloJ1"){
        $(".tooltip").text("Poblado J1");
    }
    else if (this.id == "puebloJ2"){
        $(".tooltip").text("Poblado J2");
    }
    else if (this.id == "puebloJ3"){
        $(".tooltip").text("Poblado J3");
    }
    else if (this.id == "puebloJ4"){
        $(".tooltip").text("Poblado J4");
    }
    else if (this.id == "fortaleza"){
        $(".tooltip").text("Tu Fortaleza");
    }          
}).mouseout(function(){
    hideTooltip(); 
});

$('.icono_ejercito').mouseover(function(event) {
    createTooltip(event);
    $(".tooltip").text("Tu Ejército");               
}).mouseout(function(){
    hideTooltip(); 
});

