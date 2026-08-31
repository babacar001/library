from connection import get_db
from datetime import datetime

def count_books_per_author():
    """Compte le nombre de livres par auteur."""
    db = get_db()
    pipeline = [
        {"$unwind": "$authors"},
        {"$group": {"_id": "$authors.name", "total_books": {"$sum": 1}}},
        {"$sort": {"total_books": -1}}
    ]
    
    print("\n--- Nombre de livres par auteur ---")
    results = list(db["books"].aggregate(pipeline))
    for doc in results:
        print(f" Auteur: {doc['_id']} | Nombre de livres: {doc['total_books']}")
    return results

def get_unreturned_borrowings():
    """Affiche la liste des livres empruntés et non rendus à ce jour."""
    db = get_db()
    
    if db["borrowings"].count_documents({}) == 0:
        book_clean = db["books"].find_one({"title": "Clean Code"})
        if book_clean:
            db["borrowings"].insert_one({
                "book_id": book_clean["_id"],
                "user_name": "Alice Dupont",
                "borrowed_at": datetime(2026, 8, 10),
                "due_date": datetime(2026, 8, 24),
                "returned_at": None
            })

    pipeline = [
        {
            "$match": {
                "returned_at": None,
                "due_date": {"$lt": datetime.now()}
            }
        },
        {
            "$lookup": {
                "from": "books",
                "localField": "book_id",
                "foreignField": "_id",
                "as": "book_details"
            }
        },
        {"$unwind": "$book_details"},
        {
            "$project": {
                "_id": 0,
                "title": "$book_details.title",
                "user_name": 1,
                "due_date": 1
            }
        }
    ]

    print("\n--- Livres empruntés non rendus à ce jour ---")
    results = list(db["borrowings"].aggregate(pipeline))
    for doc in results:
        print(f" Livre: '{doc['title']}' | Emprunteur: {doc['user_name']} | Date retour prévue: {doc['due_date'].strftime('%Y-%m-%d')}")
    return results

if __name__ == "__main__":
    count_books_per_author()
    get_unreturned_borrowings()