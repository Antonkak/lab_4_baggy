import random
from .book import Book, PrBook, Manga
from .library import Library
from .const import TITLES, AUTHORS, GENRES



def generate_random_book() -> Book:
    title = random.choice(TITLES)
    author = random.choice(AUTHORS)
    year = random.randint(1800, 2024)
    genre = random.choice(GENRES)
    isbn = "".join(str(random.randint(0, 9)) for _ in range(13))
    if random.choice([True, False]):
        pages = random.randint(50, 1000)
        return PrBook(title, author, year, genre, isbn, pages)
    else:
        fmt = random.choice(["pdf", "epub", "mobi"])
        return Manga(title, author, year, genre, isbn, fmt)

def format_books(books: list[Book]) -> str:
    if not books:
        return "<none>"
    return "".join(str(book) for book in books)

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)
    
    library = Library()
    all_isbns = set()
    try:
        import typer
        log = typer.echo
    except ImportError:
        log = print

    log("Simulation start")
    log(f"Steps: {steps}, Seed: {seed}")

    for step in range(1, steps + 1):
        events = []
        events.append("add")
        if len(library.books) > 0:
            events.append("remove")
        events.extend(["search_author", "search_year", "search_fake_isbn"])
        event = random.choice(events)

        if event == "add":
            book = generate_random_book()
            while book.isbn in all_isbns:
                book = generate_random_book()
            all_isbns.add(book.isbn)
            library.add_book(book)
            log(f"Step {step}  Added book: {book}")

        elif event == "remove":
            book_to_remove = random.choice(list(library.books))
            isbn = book_to_remove.isbn
            removed = library.remove_book(isbn)
            all_isbns.discard(isbn)
            log(f"Step {step}  Removed book: {removed}")

        elif event == "search_author":
            author = random.choice(AUTHORS)
            results = library.find_by_author(author)
            log(f"Step {step}  Search by author '{author}':")
            log(f"    Found: {format_books(results)}")

        elif event == "search_year":
            year = random.randint(1800, 2024)
            results = library.find_by_year(year)
            if results:
                log(f"Step {step}  Books from year {year}:")
                log(format_books(results))
            else:
                log(f"Step {step}  No books found from year {year}")

        elif event == "search_fake_isbn":
            fake_isbn = "".join(str(random.randint(0, 9)) for _ in range(13))
            while fake_isbn in all_isbns:
                fake_isbn = "".join(str(random.randint(0, 9)) for _ in range(13))
            result = library.find_by_isbn(fake_isbn)
            log(f"Step {step} ISBN lookup ({fake_isbn}): {'not found' if result is None else 'found'}")
