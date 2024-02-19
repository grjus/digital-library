from typing import Optional, Union

from fastapi import APIRouter, Depends

from models.author import Author
from routes.injectables import Injectables
from schema.author import AuthorQueryParams
from service.author_service import AuthorService

router = APIRouter()


@router.post("/add", response_description="Create a new author", response_model=Author)
async def create_author(
    author: Author, service: AuthorService = Depends(Injectables.get_author_service)
):
    return await service.create_author(author)


@router.get(
    "/{document_id}", response_description="Get an author", response_model=Author
)
async def get_author(
    document_id: str, service: AuthorService = Depends(Injectables.get_author_service)
):
    return await service.get_author(document_id)


@router.get("/", response_description="Get all authors", response_model=list[Author])
async def get_authors(
    fullname: Union[str, None] = None,
    age: Union[str, None] = None,
    email: Union[str, None] = None,
    service: AuthorService = Depends(Injectables.get_author_service),
):
    query_criteria = AuthorQueryParams(fullname=fullname, age=age, email=email)
    return await service.get_authors(query_criteria)


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
