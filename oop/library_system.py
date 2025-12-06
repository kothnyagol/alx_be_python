#!/usr/bin/python3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    "EBook: {} by {}, File Size: {}KB".format(
                        book.title,
                        book.author,
                        book.file_size
                    )
                )
            elif isinstance(book, PrintBook):
                print(
                    "PrintBook: {} by {}, Page Count: {}".format(
                        book.title,
                        book.author,
                        book.page_count
                    )
                )
            else:
                print("Book: {} by {}".format(book.title, book.author))
