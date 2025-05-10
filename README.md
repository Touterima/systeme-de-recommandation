# 🎓 Recommandation des offres de Stages

Ce projet est une application web développée avec **Flask**, **MySQL**, et **scikit-learn**. Elle permet de recommander automatiquement des offres de stage aux étudiants en fonction de leurs compétences.

---

## 🔧 Technologies utilisées

- Python 3
- Flask
- scikit-learn
- pandas
- SQLAlchemy
- MySQL

---

## 🧠 Fonctionnement

1. Les données des étudiants et des offres sont extraites de la base de données MySQL.
2. Les compétences sont vectorisées avec `TfidfVectorizer`.
3. La similarité cosinus est calculée entre le profil de l'étudiant et les offres.
4. Les 3 meilleures offres sont affichées sur la page web.
(  Interface web simple avec Flask.  )

---
## 🛠️ Stack technique

- Backend : Flask (Python)
- Machine Learning : `scikit-learn`
- Base de données : MySQL
- ORM / Connexion : SQLAlchemy + Pandas

---

## 🗃️ Structure de la base de données (`InternshipOffers`)

### Table `etudiants`

| Champ                | Type     | Description                                 |
|---------------------|----------|---------------------------------------------|
| `id`                | INT      | Identifiant unique                          |
| `name`              | VARCHAR  | Nom de l’étudiant                           |
| `major`             | VARCHAR  | Filière / spécialité                        |
| `skills`            | TEXT     | Compétences                                 |
| `preferred_location`| VARCHAR  | Localisation préférée                       |
| `desired_field`     | VARCHAR  | Domaine souhaité                            |

### Table `offre_de_stage`

| Champ         | Type     | Description                                 |
|---------------|----------|---------------------------------------------|
| `id`          | INT      | Identifiant unique                          |
| `titre`       | VARCHAR  | Titre de l’offre                            |
| `description` | TEXT     | Description du stage                        |
| `job_skills`  | TEXT     | Compétences recherchées                     |

---

## ▶️ Lancer l'application

1. Cloner le projet :
   ```bash
   git clone https://github.com/ton-utilisateur/nom-du-projet.git
   cd nom-du-projet

2.Installer les dépendances :
  pip install -r requirements.txt

3.Créer un fichier config.py :
  DB_USERNAME = 'root'
  DB_PASSWORD = ''
  DB_HOST = 'localhost'
  DB_PORT = '3306'
  DB_NAME = 'InternshipOffers'
  
4.Lancer l’application :
  python app.py

🌐 Accès
  Accueil : http://localhost:5000
  Recommandations : /api/recommendations/<nom_etudiant>

---

## ⚙️ Structure du projet

```bash
.
├── app.py              # Application Flask
├── database.py         # Connexion à la base de données
├── reco.py             # Algorithme de recommandation
├── config.py           # Informations de configuration (DB)
├── templates/          # Pages HTML (home.html, recommendations.html)
└── requirements.txt    # Dépendances Python

  
