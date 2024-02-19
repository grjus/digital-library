from pydantic import BaseModel


class AuthorQueryParams(BaseModel):
    fullname: str | None
    email: str | None
    age: str | None
    details: str | None
