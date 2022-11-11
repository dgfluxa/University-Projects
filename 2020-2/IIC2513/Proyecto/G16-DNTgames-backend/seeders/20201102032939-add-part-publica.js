'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const usuarios = await queryInterface.sequelize.query(`SELECT username FROM public.users`);
    const usuarios_ids = usuarios[0];
    await queryInterface.bulkInsert('part_publicas', [
      {
        n_part: 1,
        id_part: '0tngarrido',
        num_partidas: 10,
        n_jug: 2,
        mapa: [["1"],["2"]],
        jug:[usuarios_ids[0].username, usuarios_ids[1].username],
        createdAt: new Date(),
        updatedAt: new Date(),
      },
    
    ], {});
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
