const KoaRouter = require('koa-router');
const build_id = require('../middlewares/id');
const router = new KoaRouter();
require('dotenv').config();


router.get('teams', '/', async (ctx) => {
  const team = await ctx.db.team.findAll();
  ctx.body = team;
})

router.get('teams', '/:id', async (ctx) => {
  const team = await ctx.db.team.findByPk(ctx.params.id);
  if (!team) {
    ctx.throw(404);
  }
  ctx.body = team;
})

router.delete('teams', '/:id', async (ctx) => {
  const team = await ctx.db.team.findByPk(ctx.params.id);
  if (!team) {
    ctx.throw(404);
  }
  await team.destroy();
  ctx.status = 204;
})

router.get('teams', '/:id/players', async (ctx) => {
  const team = await ctx.db.team.findByPk(ctx.params.id);
  if (!team) {
    ctx.throw(404);
  }
  const players = await ctx.db.player.findAll({ where: { team_id: ctx.params.id} });
  ctx.body = players;
})

router.post('teams', '/:id/players', async (ctx) => {
  const { body } = ctx.request;
  const { name, age, position } = body;
  if (!name || !age || !position || typeof name != "string" || !Number.isInteger(age) || typeof position != "string") {
    ctx.throw(400);
  }
  const team = await ctx.db.team.findByPk(ctx.params.id);
  if (!team) {
    ctx.throw(422);
  }
  const player = await ctx.db.player.findOne({where: {name: name, position: position}});
  if (player) {
    ctx.body = player;
    ctx.status = 409;
  } else {
    const new_id = build_id(name, position);
    const self = process.env.BASE_URL + "/players/" + new_id;
    const team_url = process.env.BASE_URL + "/teams/" + ctx.params.id;
    const league_url = process.env.BASE_URL + "/leagues/" + team.league_id;
    const new_player = await ctx.db.player.create({
      id: new_id, 
      name: name, 
      position: position,
      age: age,
      self: self,
      team: team_url,
      league: league_url,
      times_trained: 0,
      team_id: ctx.params.id,
    });
    ctx.status = 201;
    ctx.body = new_player;
  }
})

router.put('teams', '/:id/players/train', async (ctx) => {
  const team = await ctx.db.team.findByPk(ctx.params.id);
  if (!team) {
    ctx.throw(404);
  }
  const players = await ctx.db.player.findAll({ where: { team_id: ctx.params.id} });
  for (let i=0; i < players.length; i++){
    var times_trained = players[i].times_trained + 1;
    await players[i].update({times_trained: times_trained})
  }
  ctx.status = 200;
})


module.exports = router;