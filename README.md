# 📚 DIGITAL LIBRARY MANAGEMENT SYSTEM

## 1. Project Description

This is a Python Object-Oriented Programming (OOP) console application designed to manage a digital library system using a layered architecture.

The system runs in a CLI (Command Line Interface) environment and allows users to manage books, transactions, and reports.

It supports CRUD operations, search & sorting, transaction processing, statistics generation, and SQLite database storage.

**Selected Topic:** Digital Library Management System

---

## 2. Project Objectives

- Manage library items (Books, EBooks, Audiobooks)
- Perform CRUD operations
- Search and sort data
- Handle transactions with discount system
- Store data using SQLite
- Generate reports and statistics
- Export data to CSV

---

## 3. System Architecture

DigitalLibrary/
│
├── models/   → Data Layer (Classes)
├── services/ → Business Logic Layer
├── views/    → UI Layer (Menu)
├── database/ → SQLite Storage
└── main.py

---

## 4. Database Design

### Books Table
- item_id (TEXT)
- title (TEXT)
- author (TEXT)
- book_type (TEXT)
- price (REAL)
- stock (INTEGER)
- rental_days (INTEGER)
- file_size (REAL)
- duration (INTEGER)

### Transactions Table
- transaction_id (TEXT)
- customer_name (TEXT)
- item_title (TEXT)
- quantity (INTEGER)
- total_fee (REAL)
- transaction_date (TEXT)

---

## 5. Technologies Used

- Python 3
- SQLite Database
- OOP Principles
- CLI Interface
- CSV Module
- Collections Module

---

## 6. Project Structure

DigitalLibrary/
│
├── models/
│   ├── library_item.py
│   ├── paper_book.py
│   ├── ebook.py
│   ├── audiobook.py
│   └── transaction.py
│
├── services/
│   ├── database_service.py
│   ├── library_service.py
│   ├── transaction_service.py
│   └── report_service.py
│
├── views/
│   └── menu.py
│
├── database/
│   └── library.db
│
└── main.py

---

## 7. Main Features

### 7.1 Book Management (CRUD)
- Add book
- View books
- Update book
- Delete book

### 7.2 Search & Sort
- Search by ID
- Search by title
- Sort by price (descending)

### 7.3 Transactions
- Create transaction
- Apply discount codes
- Auto update stock

### 7.4 Reports
- Revenue statistics
- Transaction statistics
- Top 3 books

### 7.5 Export
- Export CSV file

---

## 8. OOP Concepts Used

### Encapsulation
Private attributes using __variables

### Inheritance
LibraryItem → PaperBook, EBook, AudioBook

### Polymorphism
Override calculate_fee() method

### Abstraction
LibraryItem is an abstract class

---

## 9. Menu System

===== DIGITAL LIBRARY SYSTEM =====
1. Add Book
2. View Books
3. Search by ID
4. Search by Title
5. Sort Books
6. Update Book
7. Update Stock
8. Delete Book
9. Create Transaction
10. View Transactions
11. View Report
12. Export CSV
0. Exit

---

## 10. Input Validation

- Price must be ≥ 0
- Stock must be ≥ 0
- Quantity must be > 0
- ID cannot be empty
- Discount code must be valid

---

## 11. Exception Handling

- Uses try-except blocks
- Prevents invalid input crashes
- Handles database errors safely

---

## 12. Storage & Synchronization

- Automatically creates SQLite database
- Loads data on startup
- Saves data instantly after changes
- Ensures data persistence between runs

---

## 13. Advanced Features

- Transaction logic system
- Discount code system
- Inventory auto-update
- CSV export system
- Statistical reporting engine

---

## 14. How to Run

python main.py

---

## 15. Student Information

- Name: Đỗ Thanh Danh  
- Student ID: 24S7040004  
- Class: Tin 2E  
- Course: Programming Methods 1  

---

## 16. Self Assessment

| Criteria | Score |
|----------|------|
| OOP Design | 2.0 |
| CRUD System | 1.5 |
| Search & Sort | 1.0 |
| Transactions | 2.0 |
| Database | 1.0 |
| Reports | 1.0 |
| CSV Export | 0.5 |
| Exception Handling | 1.0 |
| TOTAL | 9 / 10 |
