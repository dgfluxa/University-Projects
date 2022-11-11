const KoaRouter = require('koa-router');
const build_id = require('../middlewares/id');
const router = new KoaRouter();
require('dotenv').config();


router.get('leagues', '/', async (ctx) => {
  const leagues = await ctx.db.league.findAll();
  ctx.body = leagues;
})

router.post('leagues', '/', async (ctx) => {
  const { body } = ctx.request;
  const { name, sport } = body;
  if (!name || !sport || typeof name != "string" || typeof sport != "string") {
    ctx.throw(400);
  }
  const league = await ctx.db.league.findOne({where: {name: name, sport: sport}});
  if (league) {
    ctx.body = league;
    ctx.status = 409;
  }
  else{
    const new_id = build_id(name, sport);
    const self = process.env.BASE_URL + "/leagues/" + new_id;
    const players_url = process.env.BASE_URL + "/leagues/" + new_id + "/players";
    const teams_url = process.env.BASE_URL + "/leagues/" + new_id + "/teams";
    const new_league = await ctx.db.league.create({
      id: new_id, 
      name: name, 
      sport: sport,
      self: self,
      players: players_url,
      teams: teams_url
    });
    ctx.status = 201;
    ctx.body = new_league;
  }

  
})

router.get('leagues', '/:id', async (ctx) => {
    const league = await ctx.db.league.findByPk(ctx.params.id);
    if (!league) {
      ctx.throw(404);
    }
    ctx.body = league;
})

router.delete('leagues', '/:id', async (ctx) => {
  const league = await ctx.db.league.findByPk(ctx.params.id);
  if (!league) {
    ctx.throw(404);
  }
  await league.destroy();
  ctx.status = 204;
})

router.get('leagues', '/:id/teams', async (ctx) => {
  const league = await ctx.db.league.findByPk(ctx.params.id);
  if (!league) {
    ctx.throw(404);
  }
  const teams = await ctx.db.team.findAll({ where: { league_id: ctx.params.id} });
  ctx.body = teams;
})

router.post('leagues', '/:id/teams', async (ctx) => {
  const { body } = ctx.request;
  const { name, city } = body;
  if (!name || !city || typeof name != "string" || typeof city != "string") {
    ctx.throw(400);
  }
  const league = await ctx.db.league.findByPk(ctx.params.id);
  if (!league) {
    ctx.throw(422);
  }
  const team = await ctx.db.team.findOne({where: {name: name, city: city}});
  if (team) {
    ctx.body = team;
    ctx.status = 409;
  } else {
  
    const new_id = build_id(name, city);
    const self = process.env.BASE_URL + "/teams/" + new_id;
    const players_url = process.env.BASE_URL + "/teams/" + new_id + "/players";
    const league_url = process.env.BASE_URL + "/leagues/" + ctx.params.id;
    const new_team = await ctx.db.team.create({
      id: new_id, 
      name: name, 
      city: city,
      self: self,
      players: players_url,
      league: league_url,
      league_id: ctx.params.id,
    });
    ctx.status = 201;
    ctx.body = new_team;
  }
})

router.put('leagues', '/:id/teams/train', async (ctx) => {
  const league = await ctx.db.league.findByPk(ctx.params.id);
  if (!league) {
    ctx.throw(404);
  }
  const league_teams = await ctx.db.team.findAll({ where: { league_id: ctx.params.id} });
  for (let i=0; i < league_teams.length; i++){
    var team_players = await ctx.db.player.findAll({ where: { team_id: league_teams[i].id} });
    for (let i=0; i < team_players.length; i++){
      var times_trained = team_players[i].times_trained + 1;
      await team_players[i].update({times_trained: times_trained})
    }
  }
  ctx.status = 200;
})

router.get('leagues', '/:id/players', async (ctx) => {
  const league = await ctx.db.league.findByPk(ctx.params.id);
  if (!league) {
    ctx.throw(404);
  }
  const teams = await ctx.db.team.findAll({ where: { league_id: ctx.params.id} });
  var league_players = [];
  for (let i=0; i < teams.length; i++){
    league_players = league_players.concat(await ctx.db.player.findAll({ where: { team_id: teams[i].id} }));
  }
  ctx.body = league_players;
})


module.exports = router;