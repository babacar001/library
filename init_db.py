from connection import get_db

def initialize_database():
    """Réinitialise les collections et insère les documents de départ dans Atlas."""
    db = get_db()
    books_col = db["books"]
    borrowings_col = db["borrowings"]

    # Nettoyage
    books_col.delete_many({})
    borrowings_col.delete_many({})
    print("✓ Collections réinitialisées sur MongoDB Atlas.")

    sample_books = [
        {
            "title": "Design Patterns",
            "isbn": "9780201633610",
            "publication_year": 1994,
            "available": True,
            "authors": [
                {"name": "Erich Gamma"},
                {"name": "Richard Helm"},
                {"name": "Ralph Johnson"},
                {"name": "John Vlissides"}
            ],
            "tags": ["Architecture", "Software"],
            "summary": "Elements of Reusable Object-Oriented Software."
        },
        {
            "title": "Clean Code",
            "isbn": "9780132350884",
            "publication_year": 2008,
            "available": True,
            "authors": [{"name": "Robert C. Martin"}],
            "tags": ["Clean Code", "Development"],
            "summary": "A Handbook of Agile Software Craftsmanship."
        },
        {
            "title": "The Pragmatic Programmer",
            "isbn": "9780201616224",
            "publication_year": 1999,
            "available": True,
            "authors": [{"name": "Andrew Hunt"}, {"name": "David Thomas"}],
            "tags": ["Career", "Pragmatic"],
            "summary": "Your Journey to Mastery."
        },
        {
            "title": "Designing Data-Intensive Applications",
            "isbn": "9781449373320",
            "publication_year": 2017,
            "available": True,
            "authors": [{"name": "Martin Kleppmann"}],
            "tags": ["Distributed Systems", "NoSQL", "Data"],
            "summary": "The Big Ideas Behind Reliable, Scalable, and Maintainable Systems."
        },
        {
            "title": "Refactoring",
            "isbn": "9780201485677",
            "publication_year": 1999,
            "available": True,
            "authors": [{"name": "Martin Fowler"}],
            "tags": ["Refactoring", "Clean Code"]
        }
    ]

    res = books_col.insert_many(sample_books)
    print(f"✓ {len(res.inserted_ids)} livres insérés avec succès sur Atlas.")

if __name__ == "__main__":
    initialize_database()