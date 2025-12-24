from abc import ABC, abstractmethod
class Book(ABC):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    @abstractmethod
    def get_format_info(self) -> str:
        """Возвращает информацию о формате книги."""
        pass

    def __repr__(self) -> str:
        return f'"{self.title}" by {self.author} ({self.year}) [ISBN: {self.isbn}]'

    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False


class PrBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, pages: int):
        super().__init__(title, author, year, genre, isbn)
        self.pages = pages

    def get_format_info(self) -> str:
        return f"Pr book, {self.pages} pages"

    def __repr__(self) -> str:
        base = super().__repr__()
        return f"{base} — {self.pages} pp."


class Manga(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, file_format: str):
        super().__init__(title, author, year, genre, isbn)
        self.file_format = file_format.lower()

    def get_format_info(self) -> str:
        return f"Manga, format: {self.file_format}"

    def __repr__(self) -> str:
        base = super().__repr__()
        return f"{base} — {self.file_format.upper()}"