from datetime import datetime

from models.transaction import Transaction

from services.database_service import DatabaseService


class TransactionService:

    # ==========================
    # Discount Codes
    # ==========================

    DISCOUNT_CODES = {
        "STUDENT10": 0.10,
        "VIP20": 0.20,
        "NONE": 0.00
    }

    # ==========================
    # Create Transaction
    # ==========================

    @staticmethod
    def create_transaction(
        item_id,
        customer_name,
        quantity,
        discount_code="NONE"
    ):

        try:

            # Find book
            book = DatabaseService.get_book_by_id(
                item_id
            )

            if not book:

                print(
                    "Book not found."
                )

                return False

            # Database columns
            title = book[1]
            price = book[4]
            stock = book[5]

            # ----------------------
            # Stock Validation
            # ----------------------

            if stock is not None:

                if quantity > stock:

                    print(
                        "Not enough stock available."
                    )

                    return False

            # ----------------------
            # Calculate Fee
            # ----------------------

            total_fee = price * quantity

            # Apply Discount
            discount = (
                TransactionService
                .DISCOUNT_CODES
                .get(
                    discount_code.upper(),
                    0
                )
            )

            total_fee *= (
                1 - discount
            )

            # ----------------------
            # Generate Transaction ID
            # ----------------------

            transaction_id = (
                "T" +
                datetime.now().strftime(
                    "%Y%m%d%H%M%S"
                )
            )

            # ----------------------
            # Create Transaction Object
            # ----------------------

            transaction = Transaction(
                transaction_id,
                customer_name,
                title,
                quantity,
                total_fee
            )

            # ----------------------
            # Update Stock
            # ----------------------

            if stock is not None:

                new_stock = (
                    stock - quantity
                )

                DatabaseService.update_book_stock(
                    item_id,
                    new_stock
                )

            # ----------------------
            # Save Transaction
            # ----------------------

            DatabaseService.insert_transaction(
                transaction
            )

            print(
                "Transaction created successfully."
            )

            return True

        except Exception as e:

            print(
                "Error:",
                e
            )

            return False

    # ==========================
    # Read Transactions
    # ==========================

    @staticmethod
    def get_all_transactions():

        return (
            DatabaseService
            .get_all_transactions()
        )

    # ==========================
    # Display Transactions
    # ==========================

    @staticmethod
    def display_transactions(
        transactions
    ):

        if not transactions:

            print(
                "No transactions found."
            )

            return

        for transaction in transactions:

            print("\n" + "-" * 60)

            print(
                f"Transaction ID: "
                f"{transaction[0]}"
            )

            print(
                f"Customer: "
                f"{transaction[1]}"
            )

            print(
                f"Book: "
                f"{transaction[2]}"
            )

            print(
                f"Quantity: "
                f"{transaction[3]}"
            )

            print(
                f"Total Fee: "
                f"${transaction[4]:.2f}"
            )

            print(
                f"Date: "
                f"{transaction[5]}"
            )