from connection import get_db
from pymongo import ASCENDING

def create_indexes():
    """Crée les index sur MongoDB Atlas."""
    db = get_db()
    books_col = db["books"]

    # Index simple
    index_title = books_col.create_index([("title", ASCENDING)])
    print(f"✓ Index simple créé sur 'title' : {index_title}")

    # Index composé
    index_compound = books_col.create_index([("available", ASCENDING), ("tags", ASCENDING)])
    print(f"✓ Index composé créé sur ('available', 'tags') : {index_compound}")

if __name__ == "__main__":
    create_indexes()