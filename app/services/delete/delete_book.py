from json import load, dump
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent.parent.resolve()
FILE = f"{base_dir}\\books.json"

def delete_book_by_id(book_id) -> int:
    with open(FILE, 'r') as file:
        books = load(file)
        file.close()
    new_books = [
        book for book in books
        if int(book['id']) != int(book_id)
    ]
    with open(FILE, 'w') as file:
        dump(new_books, file, indent=4)
        file.close()

    return len(new_books)