from abc import ABC, abstractmethod
from typing import Dict, List, TypeVar
from typing import Generic

from schema.author import AuthorQueryParams


T = TypeVar("T")


class Repository(Generic[T], ABC):
    @abstractmethod
    async def find_all(self, query_criteria: AuthorQueryParams | None) -> List[T]:
        pass

    @abstractmethod
    async def find(self, query_criteria: AuthorQueryParams | None) -> T:
        pass

    @abstractmethod
    async def delete(self, query_criteria: AuthorQueryParams | None) -> bool:
        pass

    @abstractmethod
    async def update(self, query_criteria: AuthorQueryParams, update: T) -> T:
        pass

    @abstractmethod
    async def create(self, new_entity: T) -> T:
        pass
