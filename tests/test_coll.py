from src.book import PrBook
from src.collections import BookCollection, IndexDict

def test_bookcollection_and_indexdict():
    coll = BookCollection()
    idx = IndexDict()
    
    book = PrBook("Test", "Author", 2020, "Fiction", "123", 100)
    coll.add(book)
    assert len(coll) == 1
    assert coll[0] == book
    
    idx.add_book(book)
    assert idx.find_by_isbn("123") == book
    assert idx.find_by_author("Author") == [book]
    assert idx.find_by_year(2020) == [book]
    
    idx.remove_book(book)
    assert idx.find_by_isbn("123") is None