"""This module contains the repository for the author model."""
from bson import ObjectId

from database.repository import Repository
from exceptions import NotFoundException
from models.author import Author
from schema.author import AuthorQueryParams


class AuthorRepository(Repository):
    def __init__(self):
        self.collection = Author

    async def find_all(self, query_criteria: AuthorQueryParams) -> list[Author]:
        q_filter = (
            query_criteria.model_dump(exclude_defaults=True, exclude_unset=True)
            if query_criteria
            else {}
        )
        authors = await self.collection.find(q_filter).to_list(10)
        return authors

    async def find(self, document_id: str) -> Author:
        author = await self.collection.get(ObjectId(document_id))
        if not author:
            raise NotFoundException("Author not found")
        return author

    async def delete(self, document_id: str) -> bool:
        author = await self.collection.get(ObjectId(document_id))
        if not author:
            raise NotFoundException("Author not found")
        result = await self.collection.delete(author)
        return result.deleted_count > 0

    async def update(self, document_id: str, update: Author) -> Author:
        author = await self.collection.get(ObjectId(document_id))
        if not author:
            raise NotFoundException("Author not found")
        await author.set({**update.model_dump()})
        return author

    async def create(self, new_entity: Author) -> Author:
        return await self.collection.insert(new_entity)
