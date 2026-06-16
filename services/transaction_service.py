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

            book_type = book[3]

            if book_type == "PaperBook":

                total_fee = (
                    price * quantity
                )

            elif book_type == "EBook":

                file_size = book[7]

                total_fee = (
                    price +
                    (file_size * 0.10)
                ) * quantity

            elif book_type == "AudioBook":

                file_size = book[7]
                duration = book[8]

                total_fee = (
                    price +
                    (file_size * 0.10) +
                    (duration * 0.05)
                ) * quantity

            else:

                total_fee = (
                    price * quantity
                )

            # ----------------------
            # Discount Validation
            # ----------------------

            if discount_code.upper() not in TransactionService.DISCOUNT_CODES:

                print(
                    "Invalid discount code. Using NONE."
                )

                discount_code = "NONE"

            discount = (
                TransactionService
                .DISCOUNT_CODES[
                    discount_code.upper()
                ]
            )

            # ----------------------
            # Apply Discount
            # ----------------------

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

            print("\n" + "=" * 50)
            print("INVOICE")
            print("=" * 50)

            print(f"Transaction ID : {transaction_id}")
            print(f"Customer       : {customer_name}")
            print(f"Book           : {title}")
            print(f"Quantity       : {quantity}")
            print(f"Unit Price     : ${price:.2f}")

            print(f"Subtotal       : ${price * quantity:.2f}")

            print(f"Discount Code  : {discount_code}")
            print(f"Discount       : {discount * 100:.0f}%")

            print(f"Total Fee      : ${total_fee:.2f}")

            if stock is not None:
                print(f"Remaining Stock: {new_stock}")

            print("=" * 50)
            print("Transaction created successfully.")

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
    def display_transactions(transactions):

        if not transactions:

            print("No transactions found.")
            return

        print("\n" + "=" * 120)

        print(
            f"{'Transaction ID':<25}"
            f"{'Customer':<20}"
            f"{'Book':<25}"
            f"{'Qty':<8}"
            f"{'Total Fee':<15}"
            f"{'Date':<25}"
        )

        print("=" * 120)

        for transaction in transactions:

            print(
                f"{str(transaction[0]):<25}"
                f"{str(transaction[1]):<20}"
                f"{str(transaction[2]):<25}"
                f"{str(transaction[3]):<8}"
                f"${float(transaction[4]):<14.2f}"
                f"{str(transaction[5]):<25}"
            )

        print("=" * 120)