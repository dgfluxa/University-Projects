
const KoaRouter = require('koa-router');
const router = new KoaRouter();
const bcrypt = require('bcrypt');
const userAuth = require('../middlewares/session');
const userGuard = require('../middlewares/users');
const jwt = require('jsonwebtoken');
const saltRounds = 10;
const TOKEN_SECRET = 'dntgames-2020';
//un usuario puede ver el perfil de otro usuario
router.get('users', '/:username', userAuth, async (ctx) => {
    const user = await ctx.db.user.findOne({where: {username: ctx.params.username,}});
    ctx.body = user;
  })

router.get('users', '/', async (ctx) => {
    const users = await ctx.db.user.findAll();
    ctx.body = users;
})

router.post('users.new', '/new', async (ctx) => {
    const { body } = ctx.request;
    const { username, password } = body;

    const user = await ctx.db.user.findOne({where: {username: username,}});
    if(user){
      ctx.body = {
          msg: "Ya existe un usuario con este username"
      };
    }
    else{
      const clave_segura =  bcrypt.hashSync(password, saltRounds);
      body.password = clave_segura;
      const new_user = await ctx.db.user.create(body);
      const token = jwt.sign({ username }, TOKEN_SECRET);
      await new_user.update({token});
      ctx.body = {
        msg: "Haz iniciado sesión correctamente",
        user: {token, username},
      };
    }

    
 })

 //un usuario no puede actualizar información de otro usuario
 router.patch('users.update', '/:id', userAuth, userGuard, async (ctx) => {
  const body = await ctx.request.body;
  const {currentUser} = ctx;
  //const clave_segura =  bcrypt.hashSync(body.password, saltRounds);
  //body.password = clave_segura;
  //const user = await ctx.db.user.findByPk(ctx.params.id);
  await currentUser.update(body);
  ctx.body = currentUser;
})
 module.exports = router;