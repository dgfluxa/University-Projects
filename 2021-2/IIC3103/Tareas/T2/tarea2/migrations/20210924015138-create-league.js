'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('leagues', {
      id: {
        allowNull: false,
        primaryKey: true,
        type: Sequelize.STRING
      },
      name: {
        type: Sequelize.STRING
      },
      sport: {
        type: Sequelize.STRING
      },
      teams: {
        type: Sequelize.STRING
      },
      players: {
        type: Sequelize.STRING
      },
      self: {
        type: Sequelize.STRING
      }
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('leagues');
  }
};