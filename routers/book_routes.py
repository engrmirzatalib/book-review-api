from fastapi import APIRouter
from models.book import Book
from database.database import books

router = APIRouter()

@router.get("/books")
def get_books():
    return books

@router.post("/books")
def create_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully"}
