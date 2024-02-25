import random
import re

from beanie import Link
from bson import DBRef
from faker import Faker

from models.author import Author
from models.book import Book, BookCategory

# DATABASE_URL = mongodb://host.docker.internal:27017/


class MockData:
    def __init__(self):
        self.fake = Faker()

    def _get_mock_author(self) -> Author:
        full_name = self.fake.name()
        return Author(
            fullname=full_name,
            age=self.fake.random_int(min=18, max=100),
            email=re.sub(r"[-_.\s]", "", full_name).lower() + "@example.com",
            details=self.fake.text(),
        )

    def get_author_list(self, count: int) -> list[Author]:
        return [self._get_mock_author() for _ in range(count)]

    def _get_random_book_category(self) -> BookCategory:
        return self.fake.random_element(BookCategory)

    def _get_mock_book(self) -> Book:
        return Book(
            title=self.fake.text(max_nb_chars=20).replace("", ""),
            year=self.fake.year(),
            quantity=self.fake.random_int(min=1, max=10),
            author_ids=[],
            category=self._get_random_book_category(),
        )

    def get_book_list(self, count: int) -> list[Book]:
        return [self._get_mock_book() for _ in range(count)]


async def populate_mock_data() -> None:
    await Author.delete_all()
    await Book.delete_all()
    mock_data = MockData()
    authors = mock_data.get_author_list(200)
    books = mock_data.get_book_list(100)
    await Author.insert_many(authors)
    inserted_authors = await Author.find_all().to_list()

    for book in books:
        random_author = random.choice(inserted_authors)
        author_id = Link(DBRef("Author", random_author.id), document_class=Author)
        book.author_ids.append(author_id)
    await Book.insert_many(books)
