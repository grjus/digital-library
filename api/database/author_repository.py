"""This module contains the repository for the author model."""
from models.author import Author

author_collcation = Author


async def add_author(new_author: Author) -> Author:
    author = await new_author.create()
    return author
