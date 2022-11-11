'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class part_publica extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  part_publica.init({
    n_part: DataTypes.INTEGER,
    id_part: DataTypes.STRING,
    num_partidas: DataTypes.INTEGER,
    n_jug: DataTypes.INTEGER,
    mapa: DataTypes.ARRAY(DataTypes.ARRAY(DataTypes.STRING)),
    jug: DataTypes.ARRAY(DataTypes.STRING)
  }, {
    sequelize,
    modelName: 'part_publica',
  });
  return part_publica;
};