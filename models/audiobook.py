from models.library_item import LibraryItem


class AudioBook(LibraryItem):

    def __init__(
        self,
        item_id,
        title,
        author,
        price,
        stock,
        rental_days,
        file_size,
        duration
    ):

        super().__init__(
            item_id,
            title,
            author,
            price
        )

        self.__stock = stock
        self.__rental_days = rental_days
        self.__file_size = file_size
        self.__duration = duration

    # ==========================
    # Encapsulation
    # ==========================

    @property
    def stock(self):
        return self.__stock

    @property
    def rental_days(self):
        return self.__rental_days

    @property
    def file_size(self):
        return self.__file_size

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):

        if value <= 0:
            raise ValueError(
                "Duration must be greater than 0."
            )

        self.__duration = value

    # ==========================
    # Polymorphism
    # ==========================

    def calculate_fee(self):

        return self.price * 1.10

    # ==========================
    # Display Methods
    # ==========================

    def display_info(self):

        return (
            f"[AudioBook] "
            f"ID: {self.item_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Price: ${self.price:.2f} | "
            f"Stock: {self.stock} | "
            f"Rental Days: {self.rental_days} | "
            f"File Size: {self.file_size} MB | "
            f"Duration: {self.duration} minutes"
        )

    def __str__(self):

        return self.display_info()