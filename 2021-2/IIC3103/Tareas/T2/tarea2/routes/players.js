const KoaRouter = require('koa-router');
const router = new KoaRouter();


router.get('players', '/', async (ctx) => {
  const players = await ctx.db.player.findAll();
  ctx.body = players;
})

router.get('players', '/:id', async (ctx) => {
    const player = await ctx.db.player.findByPk(ctx.params.id);
    if (!player) {
      ctx.throw(404);
    }
    ctx.body = player;
})

router.delete('players', '/:id', async (ctx) => {
  const player = await ctx.db.player.findByPk(ctx.params.id);
  if (!player) {
    ctx.throw(404);
  }
  await player.destroy();
  ctx.status = 204;
})

router.put('players', '/:id/train', async (ctx) => {
  const player = await ctx.db.player.findByPk(ctx.params.id);
  if (!player) {
    ctx.throw(404);
  }
  const times_trained = player.times_trained + 1;
  await player.update({times_trained: times_trained})
  ctx.status = 200;
})


module.exports = router;