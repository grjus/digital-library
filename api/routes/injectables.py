from models.author import Author
from service.author_service import AuthorService


class Injectables:
    @staticmethod
    def get_author_service():
        return AuthorService(Author)
