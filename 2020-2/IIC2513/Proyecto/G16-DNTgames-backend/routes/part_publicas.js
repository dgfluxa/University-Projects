const KoaRouter = require('koa-router');
const router = new KoaRouter();
const userAuth = require('../middlewares/session');
const userGuard = require('../middlewares/users');

router.get('part_publicas', '/:id', userAuth, async (ctx) => {
    const publica = await ctx.db.part_publica.findByPk(ctx.params.id);
    ctx.body = publica;
  })

router.get('part_publicas', '/', userAuth, async (ctx) => {
    const publica = await ctx.db.part_publica.findAll();
    ctx.body = publica;
  })

router.post('part_publicas.new', '/new', userAuth, async (ctx) => {
    const body = await ctx.request.body;
    const new_publica = await ctx.db.part_publica.create(body);
    ctx.body = new_publica;
 })

 
router.patch('part_publicas.update', '/update/:id', async (ctx) => {
  const body = await ctx.request.body;
  const partida = await ctx.db.part_publica.findByPk(ctx.params.id);
  await partida.update(body);
  ctx.body = partida;
})

 module.exports = router;