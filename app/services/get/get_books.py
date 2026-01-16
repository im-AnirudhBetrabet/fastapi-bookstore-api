from json import load
from typing import List, Dict
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent.parent.resolve()
FILE = f"{base_dir}\\books.json"

def get_books() -> List[Dict]:
    with open(FILE, 'r') as file:
        books_data = load(file)
        file.close()
    return books_data

def get_books_by_id(book_id) -> List[Dict]:
    with open(FILE, 'r') as file:
        books_data = load(file)
        book       = [book for book in books_data if int(book['id']) == int(book_id)]
    return book