function generar_bandido(jugador){
    var salud_b = Math.floor(Math.random() * (1.2 * jugador.salud)) + (0.4*jugador.salud);
    var ataque_b = Math.floor(Math.random() * (1.2 * jugador.ataque)) + (0.4*jugador.ataque);
    var defensa_b = Math.floor(Math.random() * (1.2 * jugador.defensa)) + (0.4*jugador.defensa);
  
    var bandido = {"salud": salud_b, "ataque": ataque_b, "defensa": defensa_b};
  
    return bandido;
  
  };
  
  function calcular_poder(j1, j2){
    return Math.max(1, Math.max(0, j1.ataque - j2.defensa) + (j1.salud * 0.5));
  };
  
  async function generar_respuesta(turno, ctx){
  
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
  
    var respuesta = {
        'jugador': {
            'username': turno.jugador.username,
            'id_jug': turno.jugador.id_jug,
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
        'turnos_partida': turno.turnos_partida - 1,
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
        respuesta.mapa_lugares[turno.jugada.y][turno.jugada.x] = dict[respuesta.jugador.id_jug];  
        respuesta.jugada.exito_conquistar = 1;
    }
    
    /* Vemos si se desea interactuar */
    if (turno.jugada.interactuar == 1){
        
        var numero = Math.floor(Math.random() * 100) + 1;
        // Interactuar con Bosque
        if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "B"){
            if (numero > 25){
                // No hay peligro
                respuesta.jugador.madera += 20 * respuesta.jugador.obreros;
                respuesta.jugada.exito_interactuar = 1;
            }
            else{
                // Hay peligro
                var descuento = Math.floor(Math.random() * respuesta.jugador.salud/2) + respuesta.jugador.salud/5;
                respuesta.jugador.vida_actual = Math.max(respuesta.jugador.vida_actual - descuento, 0)
                respuesta.jugada.exito_interactuar = 0;
            }
        }
        // Interactuar con Mina
        else if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "M"){
            if (numero > 15){
                // No hay peligro
                respuesta.jugador.dinero += 25 * respuesta.jugador.obreros;
                respuesta.jugada.exito_interactuar = 1;
            }
            else{
                // Hay peligro
                var descuento = Math.floor(Math.random() * respuesta.jugador.salud/4 * 3) + respuesta.jugador.salud/4;
                respuesta.jugador.vida_actual = Math.max(respuesta.jugador.vida_actual - descuento, 0)
                respuesta.jugada.exito_interactuar = 0;
            }
        }
        // Interactuar con Ruina
        else if (respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] == "R"){
            if (numero > 40){
                // No hay bandidos
                respuesta.jugada.exito_interactuar = 1;
                var dinero = Math.floor(Math.random() * 500) + 1; // Num monedas
                respuesta.jugador.dinero += dinero;
                var madera = Math.floor(Math.random() * 350) + 1; // Num madera
                respuesta.jugador.madera += madera;
                var hay_acc = Math.floor(Math.random() * 100) + 1;
                if (hay_acc > 50){
                    // Hay accesorio
  
                    var id_acc = Math.floor(Math.random() * 4) + 1;
                    const accessory = await ctx.db.accessory.findByPk(id_acc);
  
                    respuesta.jugador.accesorios.push(accessory.nombre);
  
                    respuesta.jugador.salud = Math.round(respuesta.jugador.salud * accessory.bono_salud);
                    respuesta.jugador.vida_max = respuesta.jugador.salud + 300;
                    respuesta.jugador.ataque = Math.round(respuesta.jugador.ataque * accessory.bono_ataque);
                    respuesta.jugador.defensa = Math.round(respuesta.jugador.defensa * accessory.bono_defensa);
                    respuesta.jugador.vida_actual = Math.min (respuesta.jugador.vida_actual + accessory.bono_vida, respuesta.jugador.vida_max);
                }
            }
            else{
                // Hay bandidos
  
                var bandido = generar_bandido(respuesta.jugador);
  
                var poder_jug = calcular_poder(respuesta.jugador, bandido) * ((Math.random() * 1.2) + 0.8);
                console.log(poder_jug);
                var poder_band = calcular_poder(bandido, respuesta.jugador) * ((Math.random() * 1.2) + 0.8);
                console.log(poder_band);
  
                if (poder_jug >= poder_band){
                    respuesta.jugada.exito_interactuar = 1;
                    // Se vence al bandido y se recolecta la recompensa
                    var dinero = Math.floor(Math.random() * 500) + 1; // Num monedas
                    respuesta.jugador.dinero += dinero;
                    var madera = Math.floor(Math.random() * 350) + 1; // Num madera
                    respuesta.jugador.madera += madera;
                    var hay_acc = Math.floor(Math.random() * 100) + 1;
  
                    // Calculamos actualizamos vida tras el combate
                    var daño = 0.4 * poder_band;
                    respuesta.jugador.vida_actual = Math.round(Math.max(respuesta.jugador.vida_actual - daño, 1));
                    if (hay_acc > 50){
                        // Hay accesorio
  
                        var id_acc = Math.floor(Math.random() * 4) + 1;
                        const accessory = await ctx.db.accessory.findByPk(id_acc);
  
                        respuesta.jugador.accesorios.push(accessory.nombre);
  
                        respuesta.jugador.salud = Math.round(respuesta.jugador.salud * accessory.bono_salud);
                        respuesta.jugador.vida_max = respuesta.jugador.salud + 300;
                        respuesta.jugador.ataque = Math.round(respuesta.jugador.ataque * accessory.bono_ataque);
                        respuesta.jugador.defensa = Math.round(respuesta.jugador.defensa * accessory.bono_defensa);
                        respuesta.jugador.vida_actual = Math.min (respuesta.jugador.vida_actual + accessory.bono_vida, respuesta.jugador.vida_max);
                    }
  
                    
                }
                else{
                    //Jugador pierde el combate
                    respuesta.jugada.exito_interactuar = 0;
                    // Calculamos vida tras el combate
                    respuesta.jugador.vida_actual = Math.round(Math.max(respuesta.jugador.vida_actual - poder_band, 0));
                    
                    if (respuesta.jugador.vida_actual > 0) {
                        // Calculamos unidades que mueren
                        var g_muertos = Math.round(respuesta.jugador.guerreros * (1/3));
                        var d_muertos = Math.round(respuesta.jugador.doctores * (1/3));
                        var o_muertos = Math.round(respuesta.jugador.obreros * (1/3));
  
                        // Actualizamos numero de unidades
                        respuesta.jugador.guerreros -= g_muertos;
                        respuesta.jugador.doctores -= d_muertos;
                        respuesta.jugador.obreros -= o_muertos;
  
                        // Actualizamos stats
                        respuesta.jugador.ataque -= (g_muertos*300 + d_muertos*50 + o_muertos*20);
                        respuesta.jugador.salud -= (g_muertos*300 + d_muertos*200 + o_muertos*100);
                        respuesta.jugador.defensa -= (g_muertos*200 + d_muertos*100 + o_muertos*30);
                        respuesta.jugador.vida_max = respuesta.jugador.salud + 300;
                        respuesta.jugador.vida_actual = Math.min(respuesta.jugador.vida_max, respuesta.jugador.vida_actual)
                    }
  
                }
            }
        }
        // Interactuar con poblado conquistado por otro jugador
        else if (lista.includes(respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x]) && respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] != dict[respuesta.jugador.id_jug]){
  
            // Encontramos jugador a quien pertenece el poblado
            const j2 = await ctx.db.player.findOne({where: {part_id: respuesta.id_partida, id_jug: dict2[respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x]]}});
            
            
            var poder_jug = calcular_poder(respuesta.jugador, j2) * ((Math.random() * 1.2) + 0.8);
            var poder_pob = Math.max(0, 0.6 * (j2.ataque - respuesta.jugador.defensa) + (j2.salud * 0.5));
  
            if (poder_jug > poder_pob){
                // Se vence al poblado y se conquista
                respuesta.jugada.exito_interactuar = 1;
                respuesta.jugada.exito_conquistar = 1;
                respuesta.mapa_lugares[respuesta.jugada.y][respuesta.jugada.x] = dict[respuesta.jugador.id_jug];
  
                // Actualizamos la cantidad de poblados de los jugadores
                respuesta.jugador.poblados += 1;
                j2.poblados -= 1;
  
                await ctx.db.player.update({
                    poblados: j2.poblados
                },
                { // Clause
                    where: 
                    {
                        part_id: j2.part_id,
                        id_jug: j2.id_jug
                    }
                });
  
                // Calculamos y actualizamos vida tras el combate
                var daño = 0.4 * poder_pob;
                respuesta.jugador.vida_actual = Math.round(Math.max(respuesta.jugador.vida_actual - daño, 1));
  
            }
            else{
                // Jugador pierde el combate
                respuesta.jugada.exito_interactuar = 0;
                // Calculamos vida tras el combate
                respuesta.jugador.vida_actual = Math.round(Math.max(respuesta.jugador.vida_actual - poder_pob, 0));
  
                if (respuesta.jugador.vida_actual > 0) {
                    // Calculamos unidades que mueren
                    var g_muertos = Math.round(respuesta.jugador.guerreros * (1/3));
                    var d_muertos = Math.round(respuesta.jugador.doctores * (1/3));
                    var o_muertos = Math.round(respuesta.jugador.obreros * (1/3));
  
                    // Actualizamos numero de unidades
                    respuesta.jugador.guerreros -= g_muertos;
                    respuesta.jugador.doctores -= d_muertos;
                    respuesta.jugador.obreros -= o_muertos;
  
                    // Actualizamos stats
                    respuesta.jugador.ataque -= (g_muertos*300 + d_muertos*50 + o_muertos*20);
                    respuesta.jugador.salud -= (g_muertos*300 + d_muertos*200 + o_muertos*100);
                    respuesta.jugador.vida_max = respuesta.jugador.salud + 300;
                    respuesta.jugador.defensa -= (g_muertos*200 + d_muertos*100 + o_muertos*30);
                    respuesta.jugador.vida_actual = Math.min(respuesta.jugador.vida_max, respuesta.jugador.vida_actual)
                }
  
               
            }
        }
    }
  
    /*Vemos si ha muerto */
    if (respuesta.jugador.vida_actual == 0){
        respuesta.muere = 1;
        respuesta.jugador.mapa_visitados[respuesta.jugada.y][respuesta.jugada.x] = "V";
        if (respuesta.jugador.id_jug == 1) {
            respuesta.jugada.x = 24;
            respuesta.jugada.y = 14;
        }
        else if (respuesta.jugador.id_jug == 2) {
            respuesta.jugada.x = 0;
            respuesta.jugada.y = 0;
        }
        else if (respuesta.jugador.id_jug == 3) {
            respuesta.jugada.x = 24;
            respuesta.jugada.y = 0;
        }
        else {
            respuesta.jugada.x = 0;
            respuesta.jugada.y = 14;
        }
  
  
        // Calculamos unidades que mueren
        var g_muertos = Math.round(respuesta.jugador.guerreros * (1/3));
        var d_muertos = Math.round(respuesta.jugador.doctores * (1/3));
        var o_muertos = Math.round(respuesta.jugador.obreros * (1/3));
  
        // Actualizamos numero de unidades
        respuesta.jugador.guerreros -= g_muertos;
        respuesta.jugador.doctores -= d_muertos;
        respuesta.jugador.obreros -= o_muertos;
  
        // Actualizamos stats
        respuesta.jugador.ataque -= (g_muertos*300 + d_muertos*50 + o_muertos*20);
        respuesta.jugador.salud -= (g_muertos*300 + d_muertos*200 + o_muertos*100);
        respuesta.jugador.vida_max = respuesta.jugador.salud + 300;
        respuesta.jugador.defensa -= (g_muertos*200 + d_muertos*100 + o_muertos*30);
        respuesta.jugador.vida_actual = Math.min(respuesta.jugador.vida_max, respuesta.jugador.vida_actual)
  
  
         // Calculamos poblados perdidos
        if (respuesta.jugador.poblados >= 3){
            var pob_perdidos = Math.round(respuesta.jugador.obreros * (1/3));
        }
        else if (respuesta.jugador.poblados > 0){
            var pob_perdidos = 1;
        }
        else{
            var pob_perdidos = 0;
        }
  
        // Actualizamos info de usuario
        respuesta.jugador.poblados -= pob_perdidos;
  
        var pob_camb = 0;
  
        // Actualizamos poblados en el mapa
        for (let i=1; i <= 15; i++){
            for (let j=1; j <= 25; j++){
                if (respuesta.mapa_lugares[i-1][j-1] == dict[respuesta.jugador.id_jug]){
                    respuesta.mapa_lugares[i-1][j-1] = "P";
                    pob_camb += 1
                    if (pob_camb == pob_perdidos){
                        break;
                    }
                }
            }
            if (pob_camb == pob_perdidos){
                break;
            }
        }
        respuesta.jugador.mapa_visitados[respuesta.jugada.y][respuesta.jugada.x] = "E";
    }
  
    // Actualizamos jugador en la base de datos
    await ctx.db.player.update({
        poblados: respuesta.jugador.poblados,
        vida_actual: respuesta.jugador.vida_actual,
        salud: respuesta.jugador.salud,
        ataque: respuesta.jugador.ataque,
        defensa: respuesta.jugador.defensa,
        vida_max: respuesta.jugador.vida_max,
        guerreros: respuesta.jugador.guerreros,
        doctores: respuesta.jugador.doctores,
        obreros: respuesta.jugador.obreros,
        dinero: respuesta.jugador.dinero,
        madera: respuesta.jugador.madera,
        accesorios: respuesta.jugador.accesorios,
        mapa_visitados: respuesta.jugador.mapa_visitados,
        pos_x: respuesta.jugada.x,
        pos_y: respuesta.jugada.y
  
    },
    { // Clause
        where: 
        {
            part_id: respuesta.id_partida,
            id_jug: respuesta.jugador.id_jug
        }
    });
  
    var partida = await ctx.db.part_publica.findOne({where: {id: respuesta.id_partida}});
  
    if (respuesta.jugador.id_jug == partida.n_jug){
    // Actualizamos partida en la base de datos
        await ctx.db.part_publica.update({
            // Número del jugador que le toca jugar
            n_part: 1,
  
            num_partidas: partida.num_partidas - 1,
            mapa: respuesta.mapa_lugares
  
        },
        { // Clause
            where: 
            {
                id: respuesta.id_partida
            }
        });
    }
    else{
        await ctx.db.part_publica.update({
            // Número del jugador que le toca jugar
            n_part: respuesta.jugador.id_jug + 1,
            mapa: respuesta.mapa_lugares
        },
        { // Clause
            where: 
            {
                id: respuesta.id_partida
            }
        });
    }
  
    return JSON.stringify(respuesta);
  };
  
  module.exports = generar_respuesta;