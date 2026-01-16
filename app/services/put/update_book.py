from json import load, dump
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent.parent.resolve()
FILE = f"{base_dir}\\books.json"

def update_book_by_book_id(book_id, updated_book):
    with open(FILE, 'r') as file:
        current_books = load(file)
        file.close()

    print(current_books)
    updated_book['id'] = int(book_id)

    updated_books = [
        updated_book if int(book['id']) == int(book_id)
        else book
        for book in current_books
    ]

    with open(FILE, 'w') as file:
        dump(updated_books, file, indent=4)
        file.close()

    return updated_book