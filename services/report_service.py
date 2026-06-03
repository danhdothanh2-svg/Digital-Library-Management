import csv
from collections import defaultdict

from services.database_service import DatabaseService


class ReportService:

    # ==========================
    # Total Revenue
    # ==========================

    @staticmethod
    def get_total_revenue():

        transactions = (
            DatabaseService
            .get_all_transactions()
        )

        revenue = 0

        for transaction in transactions:

            revenue += transaction[4]

        return revenue

    # ==========================
    # Total Transactions
    # ==========================

    @staticmethod
    def get_transaction_count():

        transactions = (
            DatabaseService
            .get_all_transactions()
        )

        return len(transactions)

    # ==========================
    # Average Transaction Value
    # ==========================

    @staticmethod
    def get_average_transaction():

        transactions = (
            DatabaseService
            .get_all_transactions()
        )

        if not transactions:

            return 0

        revenue = (
            ReportService
            .get_total_revenue()
        )

        return revenue / len(transactions)

    # ==========================
    # Top 3 Most Borrowed Books
    # ==========================

    @staticmethod
    def get_top_3_books():

        transactions = (
            DatabaseService
            .get_all_transactions()
        )

        book_counter = defaultdict(int)

        for transaction in transactions:

            title = transaction[2]
            quantity = transaction[3]

            book_counter[title] += quantity

        sorted_books = sorted(
            book_counter.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_books[:3]

    # ==========================
    # Display Report
    # ==========================

    @staticmethod
    def display_report():

        print("\n" + "=" * 40)
        print("LIBRARY REPORT")
        print("=" * 40)

        print(
            f"Total Revenue: "
            f"${ReportService.get_total_revenue():.2f}"
        )

        print(
            f"Total Transactions: "
            f"{ReportService.get_transaction_count()}"
        )

        print(
            f"Average Transaction Value: "
            f"${ReportService.get_average_transaction():.2f}"
        )

        print("\nTOP 3 MOST BORROWED BOOKS")

        top_books = (
            ReportService
            .get_top_3_books()
        )

        if not top_books:

            print("No transaction data.")

        else:

            for index, (
                title,
                quantity
            ) in enumerate(
                top_books,
                start=1
            ):

                print(
                    f"{index}. "
                    f"{title} "
                    f"({quantity} copies)"
                )

    # ==========================
    # Export CSV
    # ==========================

    @staticmethod
    def export_transactions_csv(
        filename="transactions_report.csv"
    ):

        transactions = (
            DatabaseService
            .get_all_transactions()
        )

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Transaction ID",
                "Customer Name",
                "Book Title",
                "Quantity",
                "Total Fee",
                "Transaction Date"
            ])

            for transaction in transactions:

                writer.writerow(transaction)

        print(
            f"CSV exported successfully: "
            f"{filename}"
        )