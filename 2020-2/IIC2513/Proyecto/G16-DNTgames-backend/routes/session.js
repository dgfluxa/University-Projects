const KoaRouter = require('koa-router');
const router = new KoaRouter();
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

//const saltRounds = 10;

const userAuth = require('../middlewares/session');

const TOKEN_SECRET = 'dntgames-2020';
router.post('session.log_in', '/log_in', async (ctx) => {

    const { body } = ctx.request;
    const { username, password } = body;

    const user = await ctx.db.user.findOne({where: {username: username,}});

    if (user){
     if(bcrypt.compareSync(password, user.password)){
        const token = jwt.sign({ username }, TOKEN_SECRET);
        const part_p = user.part_p;
        const part_g = user.part_g;
        var partida = false;
        var jugador = await ctx.db.player.findOne({where: {username: username}});
        if (jugador){
            partida = true;
        }
        await user.update({token});
        ctx.body = {
            msg: 'Has iniciado sesión correctamente',
            user: { token, username, part_g, part_p, partida },
          };
        }
     else {
            ctx.body = { error: 'Contraseña invalida' };
        }
    } else {
        ctx.body = { error: 'No existe un cliente con ese username' };
      }
})

router.delete('session.log_out', '/log_out', userAuth,async (ctx) => {
    const { currentUser } = ctx;
    currentUser.update({ token: null });
    ctx.body = { msg: 'Sesión cerrada correctamente' };
});


module.exports = router;