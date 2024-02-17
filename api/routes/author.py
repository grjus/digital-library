from fastapi import APIRouter

from models.author import Author

router = APIRouter()


@router.get("/", response_description="Health Check")
def health_check():
    return {"status": "ok"}


@router.post("/author", response_description="Add new author")
async def add_author(new_author: Author) -> Author:
    author = await new_author.create()
    return author
