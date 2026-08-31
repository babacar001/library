import os
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv

# Localise le dossier parent (racine du projet) et charge le .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

def get_db(db_name=None):
    """Établit la connexion sécurisée à MongoDB Atlas."""
    mongo_uri = os.getenv("MONGO_URI")
    
    if not mongo_uri:
        raise ValueError("⚠ Erreur : La variable MONGO_URI n'est pas chargée. Vérifiez l'emplacement du fichier .env.")

    if db_name is None:
        db_name = os.getenv("DB_NAME", "digital_library")
    
    client = MongoClient(mongo_uri)
    return client[db_name]