'use strict';

const Koa = require('koa');

require('dotenv').config();

const Router = require('koa-router');
const koaBody = require('koa-body');
const routes = require('./routes');

const app = new Koa();
const router = new Router();

app.keys = ['Shh, its a secret!'];

const db = require('./models');

const PORT = process.env.PORT || 3000

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
app.context.db = db

app.use(routes.routes());
