const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const sequelize = require('./Model/Config');
const Eleve = require('./Model/Students');
const Professeur = require('./Model/Professeur');

const app = express();

// Active CORS pour toutes les routes
app.use(cors());

app.use(bodyParser.json());

sequelize.sync()
  .then(() => console.log('Tables synchronisées'))
  .catch(err => console.error('Erreur de synchronisation:', err));

app.get('/eleves', async (req, res) => {
  try {
    const eleves = await Eleve.findAll();
    res.json(eleves);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Erreur lors de la récupération des élèves" });
  }
});

app.get('/professeurs', async (req, res) => {
  try {
    const professeurs = await Professeur.findAll();
    res.json(professeurs);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Erreur lors de la récupération des professeurs" });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Serveur lancé sur http://localhost:${PORT}`);
});
