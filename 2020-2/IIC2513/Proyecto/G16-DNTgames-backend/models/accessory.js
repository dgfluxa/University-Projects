'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class accessory extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  accessory.init({
    nombre: DataTypes.STRING,
    bono_ataque: DataTypes.FLOAT,
    bono_salud: DataTypes.FLOAT,
    bono_defensa: DataTypes.FLOAT,
    bono_vida: DataTypes.INTEGER
  }, {
    sequelize,
    modelName: 'accessory',
  });
  return accessory;
};