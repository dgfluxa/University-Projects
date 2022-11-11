const KoaRouter = require('koa-router');
const router = new KoaRouter();
const userAuth = require('../middlewares/session');
const userGuard = require('../middlewares/users');

router.get('part_privadas', '/:id', userAuth, async (ctx) => {
    const privada = await ctx.db.part_privada.findByPk(ctx.params.id);
    ctx.body = privada;
  })

router.post('part_privadas.new', '/new', userAuth, async (ctx) => {
  /* Se supone que el usuario conectado debe asociarse a un anfitrion 
  */
    const body = await ctx.request.body;
    body.anfitrion = currentUser.username;
    const new_privada = await ctx.db.part_privada.create(body);
    ctx.body = new_privada;
 })

 module.exports = router;