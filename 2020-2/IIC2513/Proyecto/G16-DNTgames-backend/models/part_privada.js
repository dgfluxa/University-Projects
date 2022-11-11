'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class part_privada extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  part_privada.init({
    n_part: DataTypes.INTEGER,
    id_part: DataTypes.STRING,
    anfitrion: DataTypes.STRING,
    num_partidas: DataTypes.INTEGER,
    n_jug: DataTypes.INTEGER,
    jug: DataTypes.ARRAY(DataTypes.STRING),
    mapa: DataTypes.ARRAY(DataTypes.ARRAY(DataTypes.STRING)),
  }, {
    sequelize,
    modelName: 'part_privada',
  });
  return part_privada;
};