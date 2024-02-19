"""This module contains the repository for the author model."""
from database.repository import Repository
from exceptions import NotFoundException
from models.author import Author
from schema.author import AuthorQueryParams


class AuthorRepository(Repository):
    def __init__(self):
        self.collection = Author

    async def find_all(self, query_criteria: AuthorQueryParams) -> list:
        filter = query_criteria.model_dump() if query_criteria else {}
        authors = await self.collection.find(filter).to_list(100)
        return authors

    async def find(self, query_criteria: AuthorQueryParams) -> Author:
        author = await self.collection.find_one(query_criteria.model_dump())
        if not author:
            raise NotFoundException("Author not found")
        return author

    async def delete(self, query_criteria: AuthorQueryParams) -> bool:
        result = await self.collection.delete(query_criteria)
        return result.deleted_count > 0

    async def update(self, query_criteria: AuthorQueryParams, update: Author) -> Author:
        author = await self.collection.update(
            query_criteria.model_dump(), {"$set": update}
        )
        return author

    async def create(self, new_entity: Author) -> Author:
        author = await self.collection.insert_one(new_entity)
        if not author:
            raise NotFoundException("Author not found")
        return author
