const userAuth = async (ctx, next) => {
    const authorization = ctx.get('Authorization');
    const token = authorization.replace('Bearer ', '');
  
    try {
      const user = await ctx.db.user.findOne({
        where: {
          token,
        },
      });
  
      if (user) {
        ctx.currentUser = user;
        return next(ctx);
      } else {
        ctx.body = { error: 'Debes iniciar sesión' };
      }
    } catch (error) {
      return (ctx.body = { error: 'Debes iniciar sesión' });
    }
  };
  
  module.exports = userAuth;