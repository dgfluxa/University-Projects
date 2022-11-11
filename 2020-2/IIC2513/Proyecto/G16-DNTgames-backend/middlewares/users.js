const userGuard = async (ctx, next) => {
    const { currentUser } = ctx;
  
    if (currentUser.dataValues.id.toString() !== ctx.params.id) {
      return (ctx.body = {
        error: 'No puedes ver/modificar información de otros clientes',
      });
    }
  
    return next(ctx);
  };
  
  module.exports = userGuard;
  