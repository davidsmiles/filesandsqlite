from typing import List, Dict, Union
from .db_conn import DatabaseConnection

"""
Concerned with storing and retrieving books from a csv file
Format of the csv file:

name,author,read
"""

Book = Dict[str, Union[str, int]]


def create_book_tables():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)')


def add_book(name: str, author: str):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_all_books() -> List[Book]:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        result = cursor.execute('SELECT * FROM books').fetchall()
        result = [{'name': row[0], 'author': row[1], 'read': row[2]}
                  for row in result]

    print(result)
    return result


def mark_book_as_read(name):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

    cursor.execute('UPDATE books SET read = ? WHERE name = ?', (1, name))


def delete_book(name):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name = ?', (name,))

