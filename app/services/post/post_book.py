import json
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent.parent.resolve()
FILE = f"{base_dir}\\books.json"

def add_book(book):
    with open(FILE, 'r') as file:
        data = json.load(file)
        file.close()
    new_id = int(sorted(data, key=lambda item: item['id'])[-1]['id'])
    book['id'] = new_id + 1
    data.append(book)
    with open(FILE, 'w') as file:
        json.dump(data, file, indent=4)
        file.close()

    return [book]