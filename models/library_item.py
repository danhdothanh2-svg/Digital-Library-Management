from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """
    Abstract parent class for all library items.
    """

    def __init__(self, item_id, title, author, price):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.price = price

    # ==========================
    # Encapsulation
    # ==========================

    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        if not value.strip():
            raise ValueError("Item ID cannot be empty.")
        self.__item_id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty.")
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not value.strip():
            raise ValueError("Author cannot be empty.")
        self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # ==========================
    # Abstraction
    # ==========================

    @abstractmethod
    def calculate_fee(self):
        """
        Must be implemented by child classes.
        """
        pass

    # ==========================
    # Common Methods
    # ==========================

    def display_info(self):
        return (
            f"ID: {self.item_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Price: ${self.price:.2f}"
        )

    def __str__(self):
        return self.display_info()