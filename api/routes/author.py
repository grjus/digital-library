from typing import Union

from fastapi import APIRouter, Depends, HTTPException

from app_exceptions import NotFoundException
from models.author import Author
from routes.injectables import Injectables
from schemas.author import AuthorDtoPageable, AuthorDtoWithDetails
from service.author_service import AuthorService

router = APIRouter()


@router.post("/add", response_description="Create a new author", response_model=Author)
async def create_author(
    author: Author, service: AuthorService = Depends(Injectables.get_author_service)
):
    return await service.create_author(author)


@router.get(
    "/{document_id}",
    response_description="Get an author",
    response_model=AuthorDtoWithDetails,
)
async def get_author(
    document_id: str, service: AuthorService = Depends(Injectables.get_author_service)
) -> AuthorDtoWithDetails:
    try:
        return await service.get_author(document_id)
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.get(
    "/", response_description="Get all authors", response_model=AuthorDtoPageable
)
async def get_authors(
    query="",
    page_size: int = 5,
    page_number: int = 0,
    service: AuthorService = Depends(Injectables.get_author_service),
) -> AuthorDtoPageable:
    return await service.get_pageable_authors_matching_query(
        page_number=page_number, page_size=page_size, query=query
    )


@router.post(
    "/update/{document_id}",
    response_description="Update author information",
    response_model=Author,
)
async def update_author(
    document_id: str,
    update: Author,
    service: AuthorService = Depends(Injectables.get_author_service),
):
    return await service.update_author(document_id, update)


@router.delete(
    "/{document_id}", response_description="Delete an author", response_model=bool
)
async def delete_author(
    document_id: str, service: AuthorService = Depends(Injectables.get_author_service)
):
    return await service.delete_author(document_id)
