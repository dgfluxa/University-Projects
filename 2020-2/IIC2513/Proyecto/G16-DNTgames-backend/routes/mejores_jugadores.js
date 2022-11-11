const KoaRouter = require('koa-router');
const router = new KoaRouter();
const userAuth = require('../middlewares/session');

router.get('mejores_jugadores', '/', async (ctx) =>{
    const privadas = await ctx.db.part_privada.findAll();
    const publicas = await ctx.db.part_publica.findAll();
    const partidas = privadas.concat(publicas);
    ctx.body = partidas;
});

module.exports = router;