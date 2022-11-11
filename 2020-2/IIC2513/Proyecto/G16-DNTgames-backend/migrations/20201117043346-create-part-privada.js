'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('part_privadas', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      n_part: {
        type: Sequelize.INTEGER
      },
      id_part: {
        type: Sequelize.STRING
      },
      anfitrion: {
        type: Sequelize.STRING
      },
      num_partidas: {
        type: Sequelize.INTEGER
      },
      n_jug: {
        type: Sequelize.INTEGER
      },
      jug: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      mapa: {
        type: Sequelize.ARRAY(Sequelize.ARRAY(Sequelize.STRING))
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('part_privadas');
  }
};