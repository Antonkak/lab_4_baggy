from .book import Book
from .collections import BookCollection, IndexDict

class Library:
    def __init__(self):
        self.books = BookCollection()
        self.index = IndexDict()

    def add_book(self, book: Book) -> None:
        self.books.add(book)
        self.index.add_book(book)

    def remove_book(self, isbn: str) -> Book:
        book = self.index.find_by_isbn(isbn)
        if book is None:
            raise KeyError(f"Book with ISBN {isbn} not in library")
        self.books.remove(isbn)
        self.index.remove_book(book)
        return book

    def find_by_isbn(self, isbn: str) -> Book | None:
        return self.index.find_by_isbn(isbn)

    def find_by_author(self, author: str) -> list[Book]:
        return self.index.find_by_author(author)

    def find_by_year(self, year: int) -> list[Book]:
        return self.index.find_by_year(year)