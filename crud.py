from connection import get_db

def insert_book(book_data):
    """Insère un nouveau livre sur MongoDB Atlas."""
    db = get_db()
    result = db["books"].insert_one(book_data)
    print(f"✓ Livre inséré sur Atlas avec l'ID : {result.inserted_id}")
    return result.inserted_id

def update_book_availability(title, available_status):
    """Met à jour la disponibilité d'un livre."""
    db = get_db()
    result = db["books"].update_one(
        {"title": title},
        {"$set": {"available": available_status}}
    )
    if result.modified_count > 0:
        print(f"✓ Statut de '{title}' mis à jour : available={available_status}")
    else:
        print(f"⚠ Aucun document modifié pour '{title}'.")
    return result.modified_count

if __name__ == "__main__":
    new_book = {
        "title": "Domain-Driven Design",
        "isbn": "9780321125217",
        "publication_year": 2003,
        "available": True,
        "authors": [{"name": "Eric Evans"}],
        "tags": ["DDD", "Architecture"],
        "summary": "Tackling Complexity in the Heart of Software."
    }
    insert_book(new_book)
    update_book_availability("Clean Code", False)