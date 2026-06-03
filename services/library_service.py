from models.paper_book import PaperBook
from models.ebook import EBook
from models.audiobook import AudioBook

from services.database_service import DatabaseService


class LibraryService:

    # ==========================
    # CREATE
    # ==========================

    @staticmethod
    def add_book(book):

        try:

            if DatabaseService.get_book_by_id(
                book.item_id
            ):

                print(
                    "Book ID already exists."
                )

                return False

            if isinstance(book, PaperBook):

                DatabaseService.insert_book(
                    book.item_id,
                    book.title,
                    book.author,
                    "PaperBook",
                    book.price,
                    book.stock,
                    book.rental_days,
                    None,
                    None
                )

            elif isinstance(book, EBook):

                DatabaseService.insert_book(
                    book.item_id,
                    book.title,
                    book.author,
                    "EBook",
                    book.price,
                    None,
                    None,
                    book.file_size,
                    None
                )

            elif isinstance(book, AudioBook):

                DatabaseService.insert_book(
                    book.item_id,
                    book.title,
                    book.author,
                    "AudioBook",
                    book.price,
                    None,
                    None,
                    None,
                    book.duration
                )

            print(
                "Book added successfully."
            )

            return True

        except Exception as e:

            print(
                "Error:",
                e
            )

            return False

    # ==========================
    # READ
    # ==========================

    @staticmethod
    def get_all_books():

        return DatabaseService.get_all_books()

    # ==========================
    # SEARCH
    # ==========================

    @staticmethod
    def search_by_id(item_id):

        return DatabaseService.get_book_by_id(
            item_id
        )

    @staticmethod
    def search_by_title(title):

        books = (
            DatabaseService.get_all_books()
        )

        results = []

        for book in books:

            if title.lower() in book[1].lower():

                results.append(book)

        return results

    # ==========================
    # UPDATE
    # ==========================

    @staticmethod
    def update_book_info(
        item_id,
        title,
        author,
        price
    ):

        book = DatabaseService.get_book_by_id(
            item_id
        )

        if not book:

            print(
                "Book not found."
            )

            return False

        DatabaseService.update_book(
            item_id,
            title,
            author,
            price
        )

        print(
            "Book information updated successfully."
        )

        return True

    @staticmethod
    def update_stock(
        item_id,
        new_stock
    ):

        book = DatabaseService.get_book_by_id(
            item_id
        )

        if not book:

            print(
                "Book not found."
            )

            return False

        DatabaseService.update_book_stock(
            item_id,
            new_stock
        )

        print(
            "Stock updated successfully."
        )

        return True

    # ==========================
    # DELETE
    # ==========================

    @staticmethod
    def delete_book(item_id):

        book = DatabaseService.get_book_by_id(
            item_id
        )

        if not book:

            print(
                "Book not found."
            )

            return False

        DatabaseService.delete_book(
            item_id
        )

        print(
            "Book deleted successfully."
        )

        return True

    # ==========================
    # SORTING
    # ==========================

    @staticmethod
    def sort_by_title():

        books = (
            DatabaseService.get_all_books()
        )

        return sorted(
            books,
            key=lambda book: book[1]
        )

    @staticmethod
    def sort_by_price_desc():

        books = (
            DatabaseService.get_all_books()
        )

        return sorted(
            books,
            key=lambda book: book[4],
            reverse=True
        )

    # ==========================
    # DISPLAY
    # ==========================

    @staticmethod
    def display_books(books):

        if not books:

            print(
                "No books found."
            )

            return

        for book in books:

            print("\n" + "-" * 50)

            print(
                f"ID: {book[0]}"
            )

            print(
                f"Title: {book[1]}"
            )

            print(
                f"Author: {book[2]}"
            )

            print(
                f"Type: {book[3]}"
            )

            print(
                f"Price: ${book[4]:.2f}"
            )

            if book[5] is not None:

                print(
                    f"Stock: {book[5]}"
                )

            if book[6] is not None:

                print(
                    f"Rental Days: {book[6]}"
                )

            if book[7] is not None:

                print(
                    f"File Size: {book[7]} MB"
                )

            if book[8] is not None:

                print(
                    f"Duration: {book[8]} minutes"
                )