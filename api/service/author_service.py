from typing import Optional

from database.repository import Repository
from models.author import Author
from schema.author import AuthorQueryParams


class AuthorService:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def get_authors(
        self, query_criteria: Optional[AuthorQueryParams]
    ) -> list[Author]:
        return await self.repository.find_all(query_criteria)

    async def get_author(self, document_id: str) -> Author:
        return await self.repository.find(document_id)

    async def delete_author(self, document_id: str) -> bool:
        return await self.repository.delete(document_id)

    async def update_author(self, document_id, update: Author) -> Author:
        return await self.repository.update(document_id, update)

    async def create_author(self, new_entity: Author) -> Author:
        return await self.repository.create(new_entity)
