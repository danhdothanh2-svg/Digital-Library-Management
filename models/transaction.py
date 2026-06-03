from datetime import datetime


class Transaction:

    def __init__(
        self,
        transaction_id,
        customer_name,
        item_title,
        quantity,
        total_fee,
        transaction_date=None
    ):

        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.item_title = item_title
        self.quantity = quantity
        self.total_fee = total_fee

        if transaction_date is None:
            self.transaction_date = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        else:
            self.transaction_date = transaction_date

    # ==========================
    # Encapsulation
    # ==========================

    @property
    def transaction_id(self):
        return self.__transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        if not value.strip():
            raise ValueError(
                "Transaction ID cannot be empty."
            )

        self.__transaction_id = value

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, value):
        if not value.strip():
            raise ValueError(
                "Customer name cannot be empty."
            )

        self.__customer_name = value

    @property
    def item_title(self):
        return self.__item_title

    @item_title.setter
    def item_title(self, value):
        if not value.strip():
            raise ValueError(
                "Item title cannot be empty."
            )

        self.__item_title = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError(
                "Quantity must be greater than 0."
            )

        self.__quantity = value

    @property
    def total_fee(self):
        return self.__total_fee

    @total_fee.setter
    def total_fee(self, value):
        if value < 0:
            raise ValueError(
                "Total fee cannot be negative."
            )

        self.__total_fee = value

    @property
    def transaction_date(self):
        return self.__transaction_date

    @transaction_date.setter
    def transaction_date(self, value):
        self.__transaction_date = value

    # ==========================
    # Utility Methods
    # ==========================

    def to_dict(self):

        return {
            "transaction_id": self.transaction_id,
            "customer_name": self.customer_name,
            "item_title": self.item_title,
            "quantity": self.quantity,
            "total_fee": self.total_fee,
            "transaction_date": self.transaction_date
        }

    def display_info(self):

        return (
            f"Transaction ID: {self.transaction_id} | "
            f"Customer: {self.customer_name} | "
            f"Book: {self.item_title} | "
            f"Quantity: {self.quantity} | "
            f"Total Fee: ${self.total_fee:.2f} | "
            f"Date: {self.transaction_date}"
        )

    def __str__(self):
        return self.display_info()