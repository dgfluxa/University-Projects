'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class league extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  league.init({
    name: DataTypes.STRING,
    sport: DataTypes.STRING,
    teams: DataTypes.STRING,
    players: DataTypes.STRING,
    self: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'league',
    underscored: true,
    timestamps: false
  });
  return league;
};