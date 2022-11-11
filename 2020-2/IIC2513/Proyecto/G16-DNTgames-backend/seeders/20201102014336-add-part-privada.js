'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    //despues, espera a que se ejecute la consulta
    const usuarios = await queryInterface.sequelize.query(`SELECT username FROM public.users`);
    const usuarios_ids = usuarios[0];
    await queryInterface.bulkInsert('part_privadas', [
      {
        n_part: 2,
        id_part: '0tngarrido',
        anfitrion: usuarios_ids[0].username,
        num_partidas: 10,
        n_jug: 2,
        mapa: "[[1],[2]]",
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
