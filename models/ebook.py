from models.library_item import LibraryItem


class EBook(LibraryItem):

    def __init__(
        self,
        item_id,
        title,
        author,
        price,
        file_size
    ):
        super().__init__(
            item_id,
            title,
            author,
            price
        )

        self.file_size = file_size

    # ==========================
    # Encapsulation
    # ==========================

    @property
    def file_size(self):
        return self.__file_size

    @file_size.setter
    def file_size(self, value):
        if value <= 0:
            raise ValueError(
                "File size must be greater than 0."
            )

        self.__file_size = value

    # ==========================
    # Polymorphism
    # ==========================

    def calculate_fee(self):
        """
        EBooks have a 5% digital service fee.
        """
        return self.price * 1.05

    # ==========================
    # Display Methods
    # ==========================

    def display_info(self):

        return (
            f"[EBook] "
            f"ID: {self.item_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Price: ${self.price:.2f} | "
            f"File Size: {self.file_size} MB"
        )

    def __str__(self):
        return self.display_info()