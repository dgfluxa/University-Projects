const KoaRouter = require('koa-router');
const router = new KoaRouter();
const userAuth = require('../middlewares/session');
const userGuard = require('../middlewares/users');

router.get('landing', '/', (ctx) => {
    var u_id = ctx.session.u_id || 0;
    
    if(u_id === 0)
       ctx.body = 'No existe un usuario conectado';
    else
       ctx.body = "Usuario " + ctx.session.username + " de id = "+ ctx.session.u_id + " se encuentra activo";
})

module.exports = router;