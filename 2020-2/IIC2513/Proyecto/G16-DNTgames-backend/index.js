'use strict';

const result = require('dotenv').config();

var session = require('koa-session');
const koa = require('koa');
const koaRouter = require('koa-router');
const koaBody = require('koa-body');
const routes = require('./routes');
// uso de CORS
//var cors = require('cors')

const app = new koa()
const router = new koaRouter()

app.keys = ['Shh, its a secret!'];
app.use(session(app));  // Include the session middleware

const db = require('./models');

const PORT = process.env.PORT || 3000;

db.sequelize
  .authenticate()
  .then(() => {
    console.log('Connection to the database has been established successfully.');
    app.listen(PORT, (err) => {
      if (err) {
        return console.error('Failed', err);
      }
      console.log(`Listening on port ${PORT}`);
      return app;
    });
  })
  .catch((err) => console.error('Unable to connect to the database:', err));



app.use(koaBody());
//app.use(cors());
app.context.db = db
app.use(routes.routes())

/*
//Probar routes
router.get('2020-2-g16-dntgames-backend', '/user/:id', async (ctx) => {
  const user = await db.user.findByPk(ctx.params.id);
  ctx.body = user;
})*/

//app.use(router.routes())
//    .use(router.allowedMethods())

//app.use(routes.routes())
//app.use(router.routes())