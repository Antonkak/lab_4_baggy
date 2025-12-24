from typing import Union
from .book import Book

class BookCollection:
    def __init__(self):
        self.books: list[Book] = []

    def add(self, book: Book) -> None:
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError(f"Book with ISBN {book.isbn} already exists")
        self.books.append(book)

    def remove(self, isbn: str) -> Book:
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                return self.books.pop(i)
        raise KeyError(f"Book with ISBN {isbn} not found")

    def __len__(self) -> int:
        return len(self.books)

    def __iter__(self):
        return iter(self.books)

    def __getitem__(self, key: Union[int, slice]):
        return self.books[key]

class IndexDict:
    def __init__(self):
        self.isbn_index: dict[str, Book] = {}
        self.author_index: dict[str, list[Book]] = {}
        self.year_index: dict[int, list[Book]] = {}

    def add_book(self, book: Book) -> None:
        self.isbn_index[book.isbn] = book
        self.author_index.setdefault(book.author, []).append(book)
        self.year_index.setdefault(book.year, []).append(book)

    def remove_book(self, book: Book) -> None:
        self.isbn_index.pop(book.isbn, None)
        if book.author in self.author_index:
            self.author_index[book.author] = [b for b in self.author_index[book.author] if b.isbn != book.isbn]
            if not self.author_index[book.author]:
                del self.author_index[book.author]
        if book.year in self.year_index:
            self.year_index[book.year] = [b for b in self.year_index[book.year] if b.isbn != book.isbn]
            if not self.year_index[book.year]:
                del self.year_index[book.year]

    def find_by_isbn(self, isbn: str) -> Book | None:
        return self.isbn_index.get(isbn)

    def find_by_author(self, author: str) -> list[Book]:
        return self.author_index.get(author, [])

    def find_by_year(self, year: int) -> list[Book]:
        return self.year_index.get(year, [])