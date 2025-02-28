const { DataTypes } = require('sequelize');
const sequelize = require('./Config');

const Eleve = sequelize.define(
  'Etudiant',
  {
    nom: { type: DataTypes.STRING },
    prenom: { type: DataTypes.STRING },
    email: { type: DataTypes.STRING },
    password: { type: DataTypes.STRING },
  },
  {
    tableName: 'Etudiant',     
    freezeTableName: true      ,
    timestamps: false,      

  }
);

module.exports = Eleve;