""" This module contains all the custom exceptions that are used in the application. """


class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
