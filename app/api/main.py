from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse

from app.services.delete.delete_book import delete_book_by_id
from app.services.get.get_books import get_books, get_books_by_id
from app.services.post.post_book import add_book
from app.services.put.update_book import update_book_by_book_id

app = FastAPI()


@app.post("/v1/books/")
async def add_new_book(book=Body()):
    new_book = add_book(book)
    return JSONResponse(
        content={
            "status_message": "Book added successfully",
            "book"          : new_book
        },
        status_code=200
    )


@app.put("/v1/books/{book_id}")
async def updated_book(book_id, book=Body()):
    try:
        book_id_to_update = int(book_id)
    except ValueError:
        return JSONResponse(
             content={
                'error_message': 'Book id must be an integer'
            },
            status_code=400
        )
    updated_book_data = update_book_by_book_id(book_id_to_update, book)
    return JSONResponse(
        content={
            "status_message": "Book updated successfully",
            "updated_book_data": updated_book_data
        },
        status_code=200
    )

@app.delete("/v1/books/{book_id}")
async def delete_book(book_id):
    try:
        book_id_to_delete = int(book_id)
    except ValueError:
        return JSONResponse(
            content={
                'error_message': 'Book id must be an integer'
            },
            status_code=400
        )
    books_remaining = delete_book_by_id(book_id_to_delete)
    return JSONResponse(
        content={
            "status_message": f"Book with id {book_id_to_delete} deleted. {books_remaining} books remain"
        },
        status_code=200
    )

@app.get("/v1/books", description="V1 version of GET route to retrieve the list of all available books in the file store")
async def get_available_books():
    books_data = get_books()
    return JSONResponse(
        content=books_data,
        status_code=200
    )

@app.get("/v1/books/{book_id}")
async def get_books_by_book_id(book_id):
    try:
        search_for_id = int(book_id)
    except ValueError:
        return JSONResponse(
            content={
                'error_message': 'Book id must be an integer'
            },
            status_code=400
        )
    return get_books_by_id(search_for_id)



@app.get("/health", description="Health Check route to check the status of the application")
async def health_check():
    return JSONResponse(
        content={
            "status": "healthy"
        },
        status_code=200
    )