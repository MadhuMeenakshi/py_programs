class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def description(self) -> str:
        return f"{self.title} by {self.author}"


def book_info() -> str:
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    return book.description()

result = book_info()
