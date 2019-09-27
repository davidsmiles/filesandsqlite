from milestone2.db import sql_db

USER_CHOICE = """
ENTER:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

"""


def prompt_add_book():
    name = input('Enter the book name: ')
    author = input("Enter the author's name: ")

    sql_db.add_book(name, author)


def list_books():
    books = sql_db.get_all_books()

    for book in books:
        name = book['name'].title()
        author = book['author'].capitalize()

        read = "YES" if book['read'] == 1 else "NO"
        print(f"{name} by {author}, read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')
    sql_db.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')
    sql_db.delete_book(name)


user_choices = {
    'a': prompt_add_book,
    'l': list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book
}


def menu():
    sql_db.create_book_tables()

    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input in user_choices.keys():
            user_choices[user_input]()
        else:
            print("Unrecognized input command")

        user_input = input(USER_CHOICE)


menu()