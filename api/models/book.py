""" This module contains the Book model. """
from typing import List

from beanie import Document, Link

from models.author import Author


class Book(Document):
    title: str
    cvategory: str
    author_ids: List[Link[Author]]
    year: int
    quantity: int

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Introduction to Python",
                "category": "Programming",
                "author_id": ["5f5e2d8d2c9c3c5b3b1b2e1b"],
                "year": 2020,
                "quantity": 10,
            }
        }

    class Settings:
        name = "book"