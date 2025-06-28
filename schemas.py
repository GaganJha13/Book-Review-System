# schemas.py

import strawberry

@strawberry.type
class BookType:
    id: int
    title: str
    author: str

@strawberry.type
class ReviewType:
    id: int
    reviewer_name: str
    rating: int
    comment: str
