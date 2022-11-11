const KoaRouter = require('koa-router');
const router = new KoaRouter();
const userAuth = require('../middlewares/session');
const userGuard = require('../middlewares/users');

router.get('accessories', '/:id', async (ctx) => {
    const accessory = await ctx.db.accessory.findByPk(ctx.params.id);
    ctx.body = accessory;
  })

module.exports = router;