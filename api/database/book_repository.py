"""This module contains the book repository which is responsible for handling all the database operations for the book model"""
from typing import List

from beanie import PydanticObjectId

from app_exceptions import NotFoundException
from models.book import Book

book_collcation = Book


async def add_book(new_book: Book) -> Book:
    book = await new_book.create()
    return book


async def retrieve_books() -> List[Book]:
    books = await book_collcation.all().to_list()
    return books


async def retrieve_book(book_id: PydanticObjectId) -> Book:
    book = await book_collcation.get(book_id)
    if book:
        return book
    raise NotFoundException(f"Book with id {book_id} not found")


async def borrow_book(book_id: PydanticObjectId, quantity: int) -> Book:
    book = await book_collcation.get(book_id)
    if book:
        if book.quantity < 0:
            raise ValueError("Not enough books to borrow")
        query = {"$inc": {"quantity": -quantity}}
        await book.update(query)
        return book
    raise NotFoundException(f"Book with id {book_id} not found")
