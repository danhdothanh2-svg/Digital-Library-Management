import sqlite3
import os


class DatabaseService:

    DB_NAME = "database/library.db"

    # ==========================
    # Database Connection
    # ==========================

    @staticmethod
    def get_connection():

        return sqlite3.connect(
            DatabaseService.DB_NAME
        )

    # ==========================
    # Initialize Database
    # ==========================

    @staticmethod
    def initialize_database():

        os.makedirs(
            "database",
            exist_ok=True
        )

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        # ==========================
        # Books Table
        # ==========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            item_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            book_type TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER,
            rental_days INTEGER,
            file_size REAL,
            duration INTEGER
        )
        """)

        # ==========================
        # Transactions Table
        # ==========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id TEXT PRIMARY KEY,
            customer_name TEXT NOT NULL,
            item_title TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            total_fee REAL NOT NULL,
            transaction_date TEXT NOT NULL
        )
        """)

        conn.commit()
        conn.close()

        print(
            "Database initialized successfully."
        )

    # ==========================
    # BOOK OPERATIONS
    # ==========================

    @staticmethod
    def insert_book(
        item_id,
        title,
        author,
        book_type,
        price,
        stock=None,
        rental_days=None,
        file_size=None,
        duration=None
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO books
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            item_id,
            title,
            author,
            book_type,
            price,
            stock,
            rental_days,
            file_size,
            duration
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_books():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM books
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_book_by_id(item_id):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM books
        WHERE item_id = ?
        """, (item_id,))

        row = cursor.fetchone()

        conn.close()

        return row

    @staticmethod
    def update_book(
        item_id,
        title,
        author,
        price
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        UPDATE books
        SET
            title = ?,
            author = ?,
            price = ?
        WHERE item_id = ?
        """, (
            title,
            author,
            price,
            item_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def update_book_stock(
        item_id,
        new_stock
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        UPDATE books
        SET stock = ?
        WHERE item_id = ?
        """, (
            new_stock,
            item_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_book(item_id):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM books
        WHERE item_id = ?
        """, (item_id,))

        conn.commit()
        conn.close()

    # ==========================
    # TRANSACTION OPERATIONS
    # ==========================

    @staticmethod
    def insert_transaction(
        transaction
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO transactions
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            transaction.transaction_id,
            transaction.customer_name,
            transaction.item_title,
            transaction.quantity,
            transaction.total_fee,
            transaction.transaction_date
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_transactions():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM transactions
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows