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
                    book.stock,
                    book.rental_days,
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
                    book.stock,
                    book.rental_days,
                    book.file_size,
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

            print("No books found.")
            return

        print("\n" + "=" * 140)

        print(
            f"{'ID':<10}"
            f"{'Title':<25}"
            f"{'Author':<20}"
            f"{'Type':<12}"
            f"{'Price':<10}"
            f"{'Stock':<8}"
            f"{'Rental':<10}"
            f"{'Size(MB)':<10}"
            f"{'Duration':<10}"
        )

        print("=" * 140)

        for book in books:

            print(
                f"{str(book[0]):<10}"
                f"{str(book[1]):<25}"
                f"{str(book[2]):<20}"
                f"{str(book[3]):<12}"
                f"{str(book[4]):<10}"
                f"{str(book[5]):<8}"
                f"{str(book[6]):<10}"
                f"{str(book[7]):<10}"
                f"{str(book[8]):<10}"
            )

        print("=" * 140)

    @staticmethod
    def update_paperbook_details(
        item_id,
        stock,
        rental_days
    ):

        DatabaseService.update_paperbook_details(
            item_id,
            stock,
            rental_days
        )

        print(
            "PaperBook updated successfully."
        )


    @staticmethod
    def update_ebook_details(
        item_id,
        stock,
        rental_days,
        file_size
    ):

        DatabaseService.update_ebook_details(
            item_id,
            stock,
            rental_days,
            file_size
        )

        print(
            "EBook updated successfully."
        )


    @staticmethod
    def update_audiobook_details(
        item_id,
        stock,
        rental_days,
        file_size,
        duration
    ):

        DatabaseService.update_audiobook_details(
            item_id,
            stock,
            rental_days,
            file_size,
            duration
        )

        print(
            "AudioBook updated successfully."
        )