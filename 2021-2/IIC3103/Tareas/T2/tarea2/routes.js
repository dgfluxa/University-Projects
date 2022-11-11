
const KoaRouter = require('koa-router');


const players = require('./routes/players');
const teams = require('./routes/teams');
const leagues = require('./routes/leagues');
const landing = require('./routes/landing');

const router = new KoaRouter();

router.use('', landing.routes());
router.use('/players', players.routes());
router.use('/teams', teams.routes());
router.use('/leagues', leagues.routes());

module.exports = router;