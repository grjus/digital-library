from bson import ObjectId

from app_exceptions import NotFoundException
from models.author import Author
from schemas.author import AuthorDto, AuthorDtoPageable, AuthorDtoWithDetails


class AuthorService:
    def __init__(self, collection: type[Author]):
        self.collection = collection

    async def get_pageable_authors_matching_query(
        self,
        page_size: int,
        page_number: int,
        query: str,
    ):
        offset = (page_number - 1) * page_size if page_number and page_size else 0

        regex_query = {"fullname": {"$regex": query, "$options": "i"}} if query else {}
        total_authors = await self.collection.find(regex_query).count()
        authors = (
            await self.collection.find(regex_query)
            .skip(offset)
            .limit(page_size)
            .to_list()
        )

        return AuthorDtoPageable(
            authors=[AuthorDto(**author.model_dump()) for author in authors],
            total_authors=total_authors,
            page_number=page_number,
            page_size=page_size,
            next_page=total_authors > offset + page_size,
        )

    async def get_author(self, document_id: str) -> AuthorDtoWithDetails:
        author = await self.collection.find_one({"_id": ObjectId(document_id)})
        if not author:
            raise NotFoundException(f"Author with id: {document_id} not found")
        if author.author_details:
            await author.fetch_link(Author.author_details)
        return AuthorDtoWithDetails(**author.model_dump())

    async def delete_author(self, document_id: str) -> bool:
        return await self.collection.delete({"_id": ObjectId(document_id)})

    async def update_author(self, document_id, update: Author) -> Author:
        return await self.collection.update(ObjectId(document_id), update)

    async def create_author(self, new_entity: Author) -> Author:
        return await self.collection.insert(new_entity)
