const KoaRouter = require('koa-router');
const router = new KoaRouter();
const userAuth = require('../middlewares/session');
const userGuard = require('../middlewares/users');
const generar_respuesta = require('../middlewares/moves');

router.post('moves', '/process', async (ctx) => {
    const body = await ctx.request.body;
    const results = await generar_respuesta(body, ctx);
    ctx.body = results;
})

router.post('moves', '/start', async (ctx) => {
    const body = await ctx.request.body;
    var jugador = await ctx.db.player.findOne({where: {username: body.username}});
    var partida = await ctx.db.part_publica.findOne({where: {id: jugador.part_id}});
    const results = JSON.stringify({
        'jugador': {
            'username': jugador.username,
            'id_jug': jugador.id_jug,
            'guerreros': jugador.guerreros,
            'doctores': jugador.doctores,
            'obreros': jugador.obreros,
            'dinero': jugador.dinero,
            'madera': jugador.madera,
            'accesorios': jugador.accesorios,
            'poblados': jugador.poblados,
            'mapa_visitados': jugador.mapa_visitados,
            'vida_actual': jugador.vida_actual,
            'vida_max': jugador.vida_max,
            'salud': jugador.salud,
            'ataque': jugador.ataque,
            'defensa': jugador.defensa
        },
        'jugada':{
            'numero': 1,  // ARREGLAR
            'x': jugador.pos_x,
            'y': jugador.pos_y,
            'interactuar': 0,
            'curar': 0,
            'conquistar': 0,
        },
        'mapa_lugares': partida.mapa,
        'id_partida': partida.id,
        'turnos_partida': partida.num_partidas
    });
    ctx.body = results;
})

router.post('moves', '/check_player', async (ctx) => {
    const body = await ctx.request.body;
    var jugador = await ctx.db.player.findOne({where: {username: body.username}});
    var partida = await ctx.db.part_publica.findOne({where: {id: jugador.part_id}});
    var results = {"correct": 0};
    if (partida.n_part == jugador.id_jug){
        results.correct = 1;
    }
    ctx.body = JSON.stringify(results);
})

router.post('moves', '/winner', async (ctx) => {
    const body = await ctx.request.body;
    
    var partida = await ctx.db.part_publica.findOne({where: {id: body.part_id}});
    var jugadores = await ctx.db.player.findAll({where: {part_id: body.part_id}});
    var winner = jugadores[0];

    if (jugadores.length == 2){
        for (var j in jugadores){
            if (jugadores[j].poblados>winner.poblados){
                winner = jugadores[j];
            }
            else if (jugadores[j].poblados == winner.poblados && jugadores[j].dinero > winner.dinero){
                winner = jugadores[j];
            }
        }
        for (var j in jugadores){
            var usuario = await ctx.db.user.findOne({where: {id: jugadores[j].user_id}});
            var perdidas = usuario.part_p + 1;
            await usuario.update({part_p: perdidas});
        }
        var us_ganador = await ctx.db.user.findOne({where: {id: winner.user_id}});
        var perdidas_g = us_ganador.part_p - 1;
        var ganadas_g = us_ganador.part_g + 1;
        
        await us_ganador.update({part_g: ganadas_g, part_p: perdidas_g})

        await partida.update({id_part: winner.username, n_jug: winner.poblados});
    }

    ctx.body = JSON.stringify({"username": partida.id_part, "poblados": partida.n_jug});
})

router.post('moves', '/end', async (ctx) => {
    const body = await ctx.request.body;
    var jugador = await ctx.db.player.findOne({where: {username: body.username}});
    var partida = await ctx.db.part_publica.findOne({where: {id: jugador.part_id}});

    const index = partida.jug.indexOf(jugador.username);
    if (index > -1) {
        partida.jug.splice(index, 1);
        await ctx.db.part_publica.update({jug: partida.jug}, {where: {id: jugador.part_id}});
        
    }

    if (partida.jug.length == 0){
        await partida.destroy()
        //await ctx.db.part_publica.destroy({where: {id: partida.id}});
    }

    await jugador.destroy()
    //await ctx.db.player.destroy({where: {username: jugador.username}});

    ctx.body = JSON.stringify(jugador);
})

module.exports = router;