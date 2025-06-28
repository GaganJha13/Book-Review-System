from sqlalchemy import Column, Integer, String, ForeignKey
from models.base import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), index=True)
    reviewer_name = Column(String)
    rating = Column(Integer)
    comment = Column(String)