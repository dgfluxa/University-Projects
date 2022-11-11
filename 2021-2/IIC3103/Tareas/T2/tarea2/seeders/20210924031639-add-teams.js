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
    const teams_arrays = [];
    teams_arrays.push({
      id: "Q2hpY2FnbyBCdWxsczpDaG",
      league_id: "TkJBOkJhc2tldGJhbGw=",
      name: "Chicago Bulls",
      city: "Chicago",
      league: "https://t2-iic3103-dgfluxa.herokuapp.com/leagues/TkJBOkJhc2tldGJhbGw=",
      players: "https://t2-iic3103-dgfluxa.herokuapp.com/teams/Q2hpY2FnbyBCdWxsczpDaG/players",
      self: "https://t2-iic3103-dgfluxa.herokuapp.com/teams/Q2hpY2FnbyBCdWxsczpDaG",
    });
    return queryInterface.bulkInsert('teams', teams_arrays);
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
