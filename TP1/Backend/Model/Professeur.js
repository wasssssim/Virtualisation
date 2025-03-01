// Model/Professeur.js
const { DataTypes } = require('sequelize');
const sequelize = require('./Config');

const Professeur = sequelize.define(
  'Professeur', 
  {
    nom: { type: DataTypes.STRING },
    prenom: { type: DataTypes.STRING },
    email: { type: DataTypes.STRING },
    password: { type: DataTypes.STRING },
  },
  {
    tableName: 'Professeur',  
    freezeTableName: true ,
    timestamps: false,       

  }
);

module.exports = Professeur;
