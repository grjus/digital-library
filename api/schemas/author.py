from typing import Optional, Union

from pydantic import BaseModel, Field, HttpUrl


class AuthorDto(BaseModel):
    id: str = Field(None, alias="id")
    fullname: str
    email: str
    age: int


class AuthorDetailsDto(BaseModel):
    bio: str
    awards: list[str]
    photo_url: HttpUrl
    published_books: list[str]
    nationality: str
    website: HttpUrl
    social_media_links: dict[str, HttpUrl]


class AuthorDtoWithDetails(AuthorDto):
    author_details: Optional[AuthorDetailsDto] = None


def to_camel(string: str) -> str:
    components = string.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


class AuthorDtoPageable(BaseModel):
    authors: list[AuthorDto]
    total_authors: int
    page_number: Union[int, None]
    page_size: Union[int, None]
    next_page: bool

    class Config:
        aliias_generator = to_camel
        populate_by_name = True
