'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('players', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      user_id: {
        type: Sequelize.INTEGER
      },
      username: {
        type: Sequelize.STRING
      },
      id_jug: {
        type: Sequelize.INTEGER
      },
      part_id:{
        type: Sequelize.INTEGER
      },
      guerreros: {
        type: Sequelize.INTEGER
      },
      doctores: {
        type: Sequelize.INTEGER
      },
      obreros: {
        type: Sequelize.INTEGER
      },
      dinero: {
        type: Sequelize.INTEGER
      },
      madera: {
        type: Sequelize.INTEGER
      },
      accesorios: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      poblados: {
        type: Sequelize.INTEGER
      },
      mapa_visitados: {
        type: Sequelize.ARRAY(Sequelize.ARRAY(Sequelize.STRING))
      },
      vida_actual: {
        type: Sequelize.INTEGER
      },
      vida_max: {
        type: Sequelize.INTEGER
      },
      salud: {
        type: Sequelize.INTEGER
      },
      ataque: {
        type: Sequelize.INTEGER
      },
      defensa: {
        type: Sequelize.INTEGER
      },
      pos_x: {
        type: Sequelize.INTEGER
      },
      pos_y: {
        type: Sequelize.INTEGER
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
    await queryInterface.dropTable('players');
  }
};