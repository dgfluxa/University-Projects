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
    const leagues_arrays = [];
    leagues_arrays.push({
      id: "TkJBOkJhc2tldGJhbGw=",
      name: "NBA",
      sport: "Basketball",
      teams: "https://t2-iic3103-dgfluxa.herokuapp.com/leagues/TkJBOkJhc2tldGJhbGw=/teams",
      players: "https://t2-iic3103-dgfluxa.herokuapp.com/leagues/TkJBOkJhc2tldGJhbGw=/players",
      self: "https://t2-iic3103-dgfluxa.herokuapp.com/leagues/TkJBOkJhc2tldGJhbGw=",
    });
    return queryInterface.bulkInsert('leagues', leagues_arrays);
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
