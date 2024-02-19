from service.author_service import AuthorService
from database.author_repository import AuthorRepository


class Injectables:
    @staticmethod
    def get_author_service():
        return AuthorService(AuthorRepository())
