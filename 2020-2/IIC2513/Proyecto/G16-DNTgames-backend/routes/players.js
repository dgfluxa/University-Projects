const KoaRouter = require('koa-router');
const router = new KoaRouter();
const userAuth = require('../middlewares/session');
const userGuard = require('../middlewares/users');

router.get('players', '/:id', async (ctx) => {
    const player = await ctx.db.player.findByPk(ctx.params.id);
    ctx.body = player;
})

router.get('players', '/', async (ctx) => {
  const player = await ctx.db.player.findAll();
  ctx.body = player;
})

router.post('players.new', '/new', userAuth, async (ctx) => {
  const body = await ctx.request.body;

  // Se crea mapa visitados
  var mapa_visitados = [];
  for (let i=1; i <= 15; i++){
      var fila = [];
      for (let j=1; j <= 25; j++){
          fila.push(0);
      }
      mapa_visitados.push(fila);
  }

  var pos_x = 0;
  var pos_y = 0;
  
  if (body.id_jug == 1) {
    pos_x = 24;
    pos_y = 14;
  }
  else if (body.id_jug == 2) {
    pos_x = 0;
    pos_y = 0;
  }
  else if (body.id_jug == 3) {
    pos_x = 24;
    pos_y = 0;
  }
  else {
    pos_x = 0;
    pos_y = 14;
  }

  mapa_visitados[pos_y][pos_x] = "E";

  var user = await ctx.db.user.findOne({where: {username: body.username}});
  var partida = await ctx.db.part_publica.findOne({where: {id: body.id_part}});
  const json = {
    'user_id': user.id,
    'id_part': body.id_part,
    'username': user.username,
    'id_jug': body.id_jug,
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
    'defensa': 0,
    "pos_x": pos_x,
    "pos_y": pos_y
  };
  const new_player = await ctx.db.player.create({user_id: user.id,
  username: user.username,
  id_jug: body.id_jug,  
  part_id: body.id_part,
  guerreros: 0,
  doctores: 0,
  obreros: 0,
  dinero: 300,
  madera: 25,
  accesorios: [],
  poblados: 0,
  mapa_visitados: mapa_visitados,
  vida_actual: 300,
  vida_max: 300,
  salud: 0,
  ataque: 0,
  defensa: 0,
  pos_x: pos_x,
  pos_y: pos_y});
  ctx.body = new_player;
})

router.post('players', '/find', async (ctx) => {
  const body = await ctx.request.body;
  var jugador = await ctx.db.player.findOne({where: {username: body.username}});
  ctx.body = JSON.stringify(jugador);
})

module.exports = router;