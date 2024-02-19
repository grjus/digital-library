from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from schema.author import AuthorQueryParams

T = TypeVar("T")


class Repository(Generic[T], ABC):
    @abstractmethod
    async def find_all(self, query_criteria: Optional[AuthorQueryParams]) -> List[T]:
        pass

    @abstractmethod
    async def find(self, document_id: str) -> T:
        pass

    @abstractmethod
    async def delete(self, document_id: str) -> bool:
        pass

    @abstractmethod
    async def update(self, document_id, update: T) -> T:
        pass

    @abstractmethod
    async def create(self, new_entity: T) -> T:
        pass
