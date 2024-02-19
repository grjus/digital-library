from typing import Union

from pydantic import BaseModel


class AuthorQueryParams(BaseModel):
    fullname: Union[str, None] = None
    email: Union[str, None] = None
    age: Union[int, None] = None
    details: Union[str, None] = None
