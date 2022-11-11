'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('players', {
      id: {
        allowNull: false,
        primaryKey: true,
        type: Sequelize.STRING
      },
      name: {
        type: Sequelize.STRING
      },
      age: {
        type: Sequelize.INTEGER
      },
      position: {
        type: Sequelize.STRING
      },
      times_trained: {
        type: Sequelize.INTEGER
      },
      league: {
        type: Sequelize.STRING
      },
      team: {
        type: Sequelize.STRING
      },
      self: {
        type: Sequelize.STRING
      }
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('players');
  }
};