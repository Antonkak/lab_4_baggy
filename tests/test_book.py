from src.book import Book, Manga, PrBook

def test_inheritance_and_polymorphism():
    pb = PrBook("A", "B", 2000, "F", "111", 100)
    eb = Manga("X", "Y", 2001, "S", "222", "pdf")
    
    assert isinstance(pb, Book)
    assert isinstance(eb, Book)
    
    assert "100 pages" in pb.get_format_info()
    assert "pdf" in eb.get_format_info().lower()

def test_book_repr_and_equality():
    b1 = PrBook("T", "A", 2020, "G", "999", 50)
    b2 = Manga("T", "A", 2020, "G", "999", "epub")
    
    assert repr(b1)
    assert b1 == b2