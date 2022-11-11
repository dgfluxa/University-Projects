const KoaRouter = require('koa-router');
const router = new KoaRouter();

router.get('landing', '/', (ctx) => {
    ctx.body = "API T2 IIC3103 Diego Fluxá";
})

module.exports = router;