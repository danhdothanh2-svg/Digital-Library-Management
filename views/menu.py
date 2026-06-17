from models.paper_book import PaperBook
from models.ebook import EBook
from models.audiobook import AudioBook

from services.library_service import LibraryService
from services.transaction_service import TransactionService
from services.report_service import ReportService


class Menu:

    @staticmethod
    def show_main_menu():

        print("\n" + "=" * 50)
        print("DIGITAL LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book by ID")
        print("4. Search Book by Title")
        print("5. Sort Books by Price (Descending)")
        print("6. Update Book Information")
        print("7. Update Book Details")
        print("8. Delete Book")

        print("\n----- Transactions -----")

        print("9. Create Transaction")
        print("10. View Transactions")

        print("\n----- Reports -----")

        print("11. View Statistics Report")
        print("12. Export CSV Report")

        print("\n0. Exit")

        return input("\nChoose: ")

    # ==========================
    # BOOK MANAGEMENT
    # ==========================

    @staticmethod
    def add_book():

        try:

            print("\nBook Types")
            print("1. Paper Book")
            print("2. EBook")
            print("3. Audio Book")

            choice = input(
                "Choose type: "
            )

            item_id = input(
                "ID: "
            )

            title = input(
                "Title: "
            )

            author = input(
                "Author: "
            )

            price = float(
                input("Price: ")
            )

            if choice == "1":

                stock = int(
                    input("Stock: ")
                )

                rental_days = int(
                    input(
                        "Rental Days: "
                    )
                )

                book = PaperBook(
                    item_id,
                    title,
                    author,
                    price,
                    stock,
                    rental_days
                )

            elif choice == "2":

                stock = int(
                    input("Stock: ")
                )

                rental_days = int(
                    input("Rental Days: ")
                )

                file_size = float(
                    input("File Size (MB): ")
                )

                book = EBook(
                    item_id,
                    title,
                    author,
                    price,
                    stock,
                    rental_days,
                    file_size
                )

            elif choice == "3":

                stock = int(
                    input("Stock: ")
                )

                rental_days = int(
                    input("Rental Days: ")
                )

                file_size = float(
                    input("File Size (MB): ")
                )

                duration = int(
                    input("Duration (minutes): ")
                )

                book = AudioBook(
                    item_id,
                    title,
                    author,
                    price,
                    stock,
                    rental_days,
                    file_size,
                    duration
                )

            else:

                print(
                    "Invalid choice."
                )

                return

            LibraryService.add_book(
                book
            )

        except ValueError:

            print(
                "Invalid input."
            )

    @staticmethod
    def view_books():

        books = (
            LibraryService
            .get_all_books()
        )

        LibraryService.display_books(
            books
        )

    @staticmethod
    def search_by_id():

        item_id = input(
            "Enter Book ID: "
        )

        book = (
            LibraryService
            .search_by_id(
                item_id
            )
        )

        if book:

            LibraryService.display_books(
                [book]
            )

        else:

            print(
                "Book not found."
            )

    @staticmethod
    def search_by_title():

        title = input(
            "Enter Title: "
        )

        books = (
            LibraryService
            .search_by_title(
                title
            )
        )

        if books:

            print("\nBook(s) found:\n")

            LibraryService.display_books(
                books
            )

        else:

            print(
                "\nBook not found."
            )

    @staticmethod
    def sort_books():

        books = (
            LibraryService
            .sort_by_price_desc()
        )

        LibraryService.display_books(
            books
        )

    @staticmethod
    def update_book_info():

        try:

            item_id = input(
                "Book ID: "
            )

            title = input(
                "New Title: "
            )

            author = input(
                "New Author: "
            )

            price = float(
                input(
                    "New Price: "
                )
            )

            LibraryService.update_book_info(
                item_id,
                title,
                author,
                price
            )

        except ValueError:

            print(
                "Invalid input."
            )

    @staticmethod
    def update_book_details():

        try:

            item_id = input(
                "Book ID: "
            )

            book = LibraryService.search_by_id(
                item_id
            )

            if not book:

                print(
                    "Book not found."
                )
                return

            book_type = book[3]

            if book_type == "PaperBook":

                stock = int(
                    input(
                        "New Stock: "
                    )
                )

                rental_days = int(
                    input(
                        "New Rental Days: "
                    )
                )

                LibraryService.update_paperbook_details(
                    item_id,
                    stock,
                    rental_days
                )

            elif book_type == "EBook":

                stock = int(
                    input("New Stock: ")
                )

                rental_days = int(
                    input("New Rental Days: ")
                )

                file_size = float(
                    input("New File Size (MB): ")
                )

                LibraryService.update_ebook_details(
                    item_id,
                    stock,
                    rental_days,
                    file_size
                )

            elif book_type == "AudioBook":

                stock = int(
                    input("New Stock: ")
                )

                rental_days = int(
                    input("New Rental Days: ")
                )

                file_size = float(
                    input("New File Size (MB): ")
                )

                duration = int(
                    input("New Duration (minutes): ")
                )

                LibraryService.update_audiobook_details(
                    item_id,
                    stock,
                    rental_days,
                    file_size,
                    duration
                )

        except ValueError:

            print(
                "Invalid input."
            )

    @staticmethod
    def delete_book():

        item_id = input(
            "Book ID: "
        )

        LibraryService.delete_book(
            item_id
        )

    # ==========================
    # TRANSACTIONS
    # ==========================

    @staticmethod
    def create_transaction():

        try:

            item_id = input(
                "Book ID: "
            )

            customer_name = input(
                "Customer Name: "
            )

            quantity = int(
                input(
                    "Quantity: "
                )
            )

            discount = input(
                "Discount Code (STUDENT10 / VIP20 / NONE): "
            )

            TransactionService.create_transaction(
                item_id,
                customer_name,
                quantity,
                discount
            )

        except ValueError:

            print(
                "Invalid input."
            )

    @staticmethod
    def view_transactions():

        transactions = (
            TransactionService
            .get_all_transactions()
        )

        TransactionService.display_transactions(
            transactions
        )

    # ==========================
    # REPORTS
    # ==========================

    @staticmethod
    def show_report():

        ReportService.display_report()

    @staticmethod
    def export_csv():

        ReportService.export_transactions_csv()