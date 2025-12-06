#!/usr/bin/python3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return "{} by {} (File Size: {}KB)".format(
            self.title, self.author, self.file_size
        )


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return "{} by {} (Page Count: {})".format(
            self.title, self.author, self.page_count
        )


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
