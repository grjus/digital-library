"""Author model."""

from beanie import Document
from pydantic import EmailStr


class Author(Document):  # pylint: disable=too-many-ancestors
    fullname: str
    email: EmailStr
    age: int
    details: str

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "George Ramzes",
                "email": "george@example.com",
                "age": 45,
                "details": "A very good author",
            }
        }

    class Settings:
        name = "author"
