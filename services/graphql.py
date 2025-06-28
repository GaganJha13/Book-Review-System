# services/graphql.py

import strawberry
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry.types import Info
from sqlalchemy import select

from models.book import Book
from models.review import Review
from schemas import BookType, ReviewType

@strawberry.type
class Query:
    @strawberry.field
    async def books(self, info: Info) -> List[BookType]:
        session: AsyncSession = info.context["session"]
        result = await session.execute(select(Book))
        books = result.scalars().all()
        return [BookType(id=book.id, title=book.title, author=book.author) for book in books]

    @strawberry.field
    async def reviews(self, info: Info, book_id: int) -> List[ReviewType]:
        session: AsyncSession = info.context["session"]
        result = await session.execute(
            select(Review).where(Review.book_id == book_id)
        )
        reviews = result.scalars().all()
        return [
            ReviewType(
                id=review.id,
                reviewer_name=review.reviewer_name,
                rating=review.rating,
                comment=review.comment
            )
            for review in reviews
        ]


@strawberry.type
class Mutation:
    @strawberry.field
    async def add_book(self, info: Info, title: str, author: str) -> BookType:
        session: AsyncSession = info.context["session"]
        book = Book(title=title, author=author)
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return BookType(id=book.id, title=book.title, author=book.author)

    @strawberry.field
    async def add_review(
        self,
        info: Info,
        book_id: int,
        reviewer_name: str,
        rating: int,
        comment: str
    ) -> ReviewType:
        session: AsyncSession = info.context["session"]
        review = Review(
            book_id=book_id,
            reviewer_name=reviewer_name,
            rating=rating,
            comment=comment
        )
        session.add(review)
        await session.commit()
        await session.refresh(review)
        return ReviewType(
            id=review.id,
            reviewer_name=review.reviewer_name,
            rating=review.rating,
            comment=review.comment
        )


schema = strawberry.Schema(query=Query, mutation=Mutation)
