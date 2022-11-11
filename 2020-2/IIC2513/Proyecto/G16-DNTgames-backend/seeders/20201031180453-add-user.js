'use strict';
const bcrypt = require('bcrypt');
const saltRounds = 10;

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const users_arrays = [];
    users_arrays.push({
      username: 'tngarrido',
      password: bcrypt.hashSync("123", saltRounds),
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    users_arrays.push({
      username: 'tgarrido',
      password: bcrypt.hashSync("123", saltRounds),
      ranking: 0,
      part_g: 0,
      part_p: 0,
      createdAt: new Date(),
      updatedAt: new Date(),
    })
    return queryInterface.bulkInsert('users', users_arrays);
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
