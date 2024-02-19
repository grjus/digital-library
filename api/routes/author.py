from fastapi import APIRouter, Depends
from models.author import Author


from routes.injectables import Injectables
from schema.author import AuthorQueryParams
from service.author_service import AuthorService

router = APIRouter()


@router.get("/", response_description="Health Check")
def health_check():
    return {"status": "ok"}


@router.post("/create", response_description="Add new author")
async def create_author(
    new_author: Author,
    author_service: AuthorService = Depends(Injectables.get_author_service),
) -> Author:
    author = await author_service.create_author(new_author)
    return author


@router.post("/all", response_description="Get all authors")
async def get_authors(
    query_params: AuthorQueryParams | None = None,
    author_service: AuthorService = Depends(Injectables.get_author_service),
) -> list:
    authors = await author_service.get_authors(query_params)
    return authors
