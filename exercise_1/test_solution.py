import pytest
from solution import Serializable, CSVMixin


def test_no_mixin(tmp_path):
    class Book(Serializable):
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def __repr__(self):
            return f"{self.title}, by {self.author}, for {self.price}"

    b = Book('title', 'author', 100)
    p = tmp_path / "hello.txt"
    b.dump(p)

    b.load(p)

    assert b.title == 'title'
    assert b.author == 'author'
    assert b.price == 100

def test_csv_mixin(tmp_path):
    class Book(CSVMixin, Serializable):
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def __repr__(self):
            return f"{self.title}, by {self.author}, for {self.price}"

    b = Book('title', 'author', 100)
    p = tmp_path / "hello.txt"
    b.dump(p)

    b.load(p)

    assert b.title == 'title'
    assert b.author == 'author'
    assert int(b.price) == 100
