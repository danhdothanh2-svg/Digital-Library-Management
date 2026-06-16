from models.library_item import LibraryItem

class PaperBook(LibraryItem):

    def __init__(
        self,
        item_id,
        title,
        author,
        price,
        stock,
        rental_days
    ):
        super().__init__(
            item_id,
            title,
            author,
            price
        )

        self.stock = stock
        self.rental_days = rental_days

    # ==========================
    # Encapsulation
    # ==========================

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError(
                "Stock cannot be negative."
            )

        self.__stock = value

    @property
    def rental_days(self):
        return self.__rental_days

    @rental_days.setter
    def rental_days(self, value):
        if value <= 0:
            raise ValueError(
                "Rental days must be greater than 0."
            )

        self.__rental_days = value

    # ==========================
    # Polymorphism
    # ==========================

    def calculate_fee(self):
        """
        Rental fee calculation for paper books.
        """
        return self.price * self.rental_days

    # ==========================
    # Display Methods
    # ==========================

    def display_info(self):

        return (
            f"[Paper Book] "
            f"ID: {self.item_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Price: ${self.price:.2f} | "
            f"Stock: {self.stock} | "
            f"Rental Days: {self.rental_days}"
        )

    def __str__(self):
        return self.display_info()