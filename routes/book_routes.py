from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models.book import Book
from models.review import Review
from services.database import get_session
from services.cache import get_books_from_cache, save_books_to_cache
from sqlalchemy import text

router = APIRouter()

@router.get("/books")
async def list_books(session: AsyncSession = Depends(get_session)):
    try:
        cached = await get_books_from_cache()
        if cached:
            return {"cached": True, "books": cached}
    except Exception:
        pass

    result = await session.execute(text("SELECT id, title, author FROM books"))
    books = [{"id": row.id, "title": row.title, "author": row.author} for row in result.fetchall()]
    await save_books_to_cache(books)
    return {"cached": False, "books": books}

@router.post("/books")
async def add_book(data: dict, session: AsyncSession = Depends(get_session)):
    book = Book(title=data["title"], author=data["author"])
    session.add(book)
    await session.commit()
    return {"message": "Book added", "book": {"title": book.title, "author": book.author}}

@router.get("/books/{book_id}/reviews")
async def get_reviews(book_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute("SELECT * FROM reviews WHERE book_id = :id", {"id": book_id})
    return result.fetchall()

@router.post("/books/{book_id}/reviews")
async def add_review(book_id: int, data: dict, session: AsyncSession = Depends(get_session)):
    review = Review(book_id=book_id, **data)
    session.add(review)
    await session.commit()
    return {"message": "Review added"}