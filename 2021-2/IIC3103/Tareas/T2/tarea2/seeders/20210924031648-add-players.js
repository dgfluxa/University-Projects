'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
    */
    const players_arrays = [];
    players_arrays.push({
      id: "TWljaGFlbCBKb3JkYW46RX",
      team_id: "Q2hpY2FnbyBCdWxsczpDaG",
      name: "Michael Jordan",
      age: 23,
      position: "Escolta",
      times_trained: 0,
      league: "https://t2-iic3103-dgfluxa.herokuapp.com/leagues/TkJBOkJhc2tldGJhbGw=",
      team: "https://t2-iic3103-dgfluxa.herokuapp.com/teams/Q2hpY2FnbyBCdWxsczpDaG",
      self: "https://t2-iic3103-dgfluxa.herokuapp.com/players/TWljaGFlbCBKb3JkYW46RX",
    });
    return queryInterface.bulkInsert('players', players_arrays);
  },

  down: async (queryInterface, Sequelize) => {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
  }
};
