## Configuration MongoDB Atlas
Créez un projet et un cluster gratuit (M0) sur MongoDB Atlas.

Dans la section Network Access, ajoutez votre adresse IP (ou 0.0.0.0/0 pour le développement).

Dans Database Access, créez un utilisateur avec les droits de lecture/écriture.

Récupérez votre chaîne de connexion (Driver Python) sous le format :
mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/...

## Installation

### Cloner le dépôt et naviguer dans le dossier :
git clone <url-du-repo>
cd Library

### Installer les dépendances :

Bash
pip install -r requirements.txt

### Créer le fichier .env depuis le modèle et renseigner la chaîne de connexion Atlas 

Éditez le fichier .env :

MONGO_URI=mongodb+srv://ton_user:ton_password@cluster0.mongodb.net/?retryWrites=true&w=majority
DB_NAME=nom_db

### Exécution des Scripts
cd src

Initialiser les collections et insérer les livres : python init_db.py

Tester les opérations CRUD : python crud.py

Lancer les agrégeurs : python aggregations.py

Créer les index : python indexes.py 
