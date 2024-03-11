import random
import re
import string

from beanie import Link
from bson import DBRef
from faker import Faker


from models.author import Author, AuthorDetails
from models.book import Book, BookCategory

# DATABASE_URL = mongodb://host.docker.internal:27017/


class MockData:
    def __init__(self):
        self.fake = Faker()

    def _get_mock_author(self) -> Author:
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        full_name = f"{first_name} {last_name}"
        return Author(
            fullname=full_name,
            age=self.fake.random_int(min=18, max=100),
            email=re.sub(r"[-_.\s]", "", full_name).lower() + "@example.com",
            short_bio=self.fake.text(),
        )
    
    def _generate_random_string(self,length=15):
        letters_and_digits = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
        return random_string

    def _get_mocked_author_details(self) -> AuthorDetails:
        fake_data = {
            "bio": self.fake.text(max_nb_chars=200),
            "awards": [
                self.fake.sentence(nb_words=4)
                for _ in range(self.fake.random_int(min=1, max=3))
            ],
            "photo_url": f"https://robohash.org/f{self._generate_random_string()}?size=400x400",
            "published_books": [
                self.fake.sentence(nb_words=5)
                for _ in range(self.fake.random_int(min=2, max=5))
            ],
            "genres": [
                self.fake.word() for _ in range(self.fake.random_int(min=2, max=4))
            ],
            "nationality": self.fake.country(),
            "website": self.fake.url(),
            "social_media_links": {
                "facebook": self.fake.url(),
                "twitter": self.fake.url(),
                "instagram": self.fake.url(),
            },
        }

        return AuthorDetails(**fake_data)

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

    def get_author_details_list(self, count: int) -> list[AuthorDetails]:
        return [self._get_mocked_author_details() for _ in range(count)]


async def populate_mock_data() -> None:
    await Author.delete_all()
    await Book.delete_all()
    await AuthorDetails.delete_all()
    mock_data = MockData()
    authors = mock_data.get_author_list(50)
    author_details = mock_data.get_author_details_list(50)
    # books = mock_data.get_book_list(100)
    await AuthorDetails.insert_many(author_details)
    # await Author.insert_many(authors)
    # inserted_authors = await Author.find_all().to_list()
    inserted_details = await AuthorDetails.find_all().to_list()
    lol = []
    for author, details in zip(authors, inserted_details):
        author.author_details = Link(
            DBRef("AuthorDetails", details.id), document_class=AuthorDetails
        )
        lol.append(author)
    await Author.insert_many(lol)

    # for book in books:
    #     random_author = random.choice(inserted_authors)
    #     author_id = Link(DBRef("Author", random_author.id), document_class=Author)
    #     book.author_ids.append(author_id)
    # await Book.insert_many(books)
