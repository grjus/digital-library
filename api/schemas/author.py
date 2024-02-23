from pydantic import BaseModel, Field


class AuthorDto(BaseModel):
    id: str = Field(None, alias="id")
    fullname: str
    email: str
    age: int
