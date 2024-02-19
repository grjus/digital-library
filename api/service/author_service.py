from database.repository import Repository
from models.author import Author
from schema.author import AuthorQueryParams


class AuthorService:
    def __init__(self, author_repository: Repository):
        self.author_repository = author_repository

    def create_author(self, author: Author):
        return self.author_repository.create(author)

    def get_authors(self, query_criteria: AuthorQueryParams | None):
        return self.author_repository.find_all(query_criteria)

    def get_author(self, query_criteria: AuthorQueryParams | None):
        return self.author_repository.find(query_criteria)

    def delete_author(self, query_criteria: AuthorQueryParams | None):
        return self.author_repository.delete(query_criteria)

    def update_author(self, query_criteria: AuthorQueryParams, update: dict):
        return self.author_repository.update(query_criteria, update)
