"""Author model."""

from typing import Optional

from beanie import Document, Link
from pydantic import EmailStr, HttpUrl

# pylint: disable=too-many-ancestors


class AuthorDetails(Document):
    bio: str
    awards: list[str]
    photo_url: HttpUrl
    published_books: list[str]
    nationality: str
    website: HttpUrl
    social_media_links: dict[str, HttpUrl]

    class Config:
        json_schema_extra = {
            "example": {
                "bio": "A short bio",
                "awards": ["award1", "award2"],
                "photo_url": "https://example.com/photo.jpg",
                "published_books": ["book1", "book2"],
                "nationality": "USA",
                "website": "https://example.com",
                "social_media_links": {
                    "facebook": "https://facebook.com",
                    "twitter": "https://twitter.com",
                    "instagram": "https://instagram.com",
                },
            }
        }

    class Settings:
        name = "author_details"


class Author(Document):  # pylint: disable=too-many-ancestors
    fullname: str
    email: EmailStr
    age: int
    short_bio: str
    author_details: Optional[Link[AuthorDetails]] = None

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "johndoe@exmaple.com",
                "age": 40,
                "short_bio": "A short bio",
                "author_details": "5f5e2d8d2c9c3c5b3b1b2e1b",
            }
        }

    class Settings:
        name = "author"
