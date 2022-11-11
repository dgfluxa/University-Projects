'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class player extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  player.init({
    name: DataTypes.STRING,
    age: DataTypes.INTEGER,
    position: DataTypes.STRING,
    times_trained: DataTypes.INTEGER,
    league: DataTypes.STRING,
    team: DataTypes.STRING,
    self: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'player',
    underscored: true,
    timestamps: false
  });
  return player;
};