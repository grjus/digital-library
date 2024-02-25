from typing import Union

from pydantic import BaseModel, Field


class AuthorDto(BaseModel):
    id: str = Field(None, alias="id")
    fullname: str
    email: str
    age: int


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
        allow_population_by_field_name = True
