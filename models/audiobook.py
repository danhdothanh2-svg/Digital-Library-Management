from models.library_item import LibraryItem


class AudioBook(LibraryItem):

    def __init__(
        self,
        item_id,
        title,
        author,
        price,
        duration
    ):
        super().__init__(
            item_id,
            title,
            author,
            price
        )

        self.duration = duration

    # ==========================
    # Encapsulation
    # ==========================

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
        """
        Audiobooks have a 10% audio service fee.
        """
        return self.price * 1.10

    # ==========================
    # Display Methods
    # ==========================

    def display_info(self):

        return (
            f"[Audio Book] "
            f"ID: {self.item_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Price: ${self.price:.2f} | "
            f"Duration: {self.duration} minutes"
        )

    def __str__(self):
        return self.display_info()