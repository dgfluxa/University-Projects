'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const accessories_arrays = [];
    accessories_arrays.push({
      id: 1,
      nombre: "Excalibur",
      bono_ataque: 2.0,
      bono_salud: 1.2,
      bono_defensa: 1.5,
      bono_vida: 0,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    accessories_arrays.push({
      id: 2,
      nombre: "Replica Excalibur",
      bono_ataque: 1.2,
      bono_salud: 1,
      bono_defensa: 1.1,
      bono_vida: 0,
      createdAt: new Date(),
      updatedAt: new Date(),
    })
    accessories_arrays.push({
      id: 3,
      nombre: "Armadura Sagrada",
      bono_ataque: 1,
      bono_salud: 1.5,
      bono_defensa: 2,
      bono_vida: 0,
      createdAt: new Date(),
      updatedAt: new Date(),
    })
    accessories_arrays.push({
      id: 4,
      nombre: "Poción Mágica de Salud",
      bono_ataque: 1,
      bono_salud: 1.8,
      bono_defensa: 1,
      bono_vida: 4000,
      createdAt: new Date(),
      updatedAt: new Date(),
    })
    return queryInterface.bulkInsert('accessories', accessories_arrays);
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
