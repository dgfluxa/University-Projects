
const KoaRouter = require('koa-router');

const users = require('./routes/users');
const part_privadas = require('./routes/part_privadas');
const part_publicas = require('./routes/part_publicas');
const mejores_jugadores = require('./routes/mejores_jugadores');
const moves = require('./routes/moves');
const players = require('./routes/players');
const accessories = require('./routes/accessories');
const session = require('./routes/session');
const landing = require('./routes/landing');

const router = new KoaRouter();

router.use('/users', users.routes());
router.use('/part_privadas', part_privadas.routes());
router.use('/part_publicas', part_publicas.routes());
router.use('/moves', moves.routes());
router.use('/players', players.routes());
router.use('/mejores_jugadores', mejores_jugadores.routes());
router.use('/accessories', accessories.routes());
router.use('', landing.routes());
router.use('/session', session.routes());

module.exports = router;