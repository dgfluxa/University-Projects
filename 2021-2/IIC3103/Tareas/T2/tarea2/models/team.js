'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class team extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      models.team.belongsTo(models.league, {foreignKey: 'league_id', as: 'father_league_id'});
      models.team.hasMany(models.player, {foreignKey: 'team_id', as: 'son_player_id'});
    }
  };
  team.init({
    name: DataTypes.STRING,
    city: DataTypes.STRING,
    league: DataTypes.STRING,
    players: DataTypes.STRING,
    self: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'team',
    underscored: true,
    timestamps: false
  });
  return team;
};