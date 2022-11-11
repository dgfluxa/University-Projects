'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    /**
     * Add altering commands here.
     *
     * Example:
     * await queryInterface.createTable('users', { id: Sequelize.INTEGER });
     */
     return queryInterface.addColumn(
       //Team belongs to league ande league has many teams
      'teams', // name of Source model
      'league_id', // name of the key we're adding 
      {
        type: Sequelize.STRING,
        references: {
          model: 'leagues', // name of Target model
          key: 'id', // key in Target model that we're referencing
        },
        onUpdate: 'CASCADE',
        onDelete: 'CASCADE',
      }
    ).then(() => {
      // Team hasMany Players and Player belongs to Team
      return queryInterface.addColumn(
        'players', // name of Target model
        'team_id', // name of the key we're adding
        {
          type: Sequelize.STRING,
          references: {
            model: 'teams', // name of Source model
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'CASCADE',
        }
      );
    });
  },

  down: async (queryInterface, Sequelize) => {
    /**
     * Add reverting commands here.
     *
     * Example:
     * await queryInterface.dropTable('users');
     */
     return queryInterface.removeColumn(
      'teams', // name of Source model
      'league_id' // key we want to remove
    ).then(() => {
      // remove Order hasMany Product
      return queryInterface.removeColumn(
        'players', // name of the Target model
        'team_id' // key we want to remove
      );
    });
  }
};
