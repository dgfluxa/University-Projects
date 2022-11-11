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
    user_id: DataTypes.INTEGER,
    username: DataTypes.STRING,
    id_jug: DataTypes.INTEGER,
    part_id: DataTypes.INTEGER,
    guerreros: DataTypes.INTEGER,
    doctores: DataTypes.INTEGER,
    obreros: DataTypes.INTEGER,
    dinero: DataTypes.INTEGER,
    madera: DataTypes.INTEGER,
    accesorios: DataTypes.ARRAY(DataTypes.STRING),
    poblados: DataTypes.INTEGER,
    mapa_visitados: DataTypes.ARRAY(DataTypes.ARRAY(DataTypes.STRING)),
    vida_actual: DataTypes.INTEGER,
    vida_max: DataTypes.INTEGER,
    salud: DataTypes.INTEGER,
    ataque: DataTypes.INTEGER,
    defensa: DataTypes.INTEGER,
    pos_x: DataTypes.INTEGER,
    pos_y: DataTypes.INTEGER
  }, {
    sequelize,
    modelName: 'player',
  });

  return player;
};

