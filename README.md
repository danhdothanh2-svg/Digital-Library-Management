# 📚 DIGITAL LIBRARY MANAGEMENT SYSTEM

## 1. Project Description

The **Digital Library Management System** is a Python-based Object-Oriented Programming (OOP) application developed as a final project for the Programming Methods course.

The system manages three different types of library items:

* Paper Books
* EBooks
* AudioBooks

It supports complete CRUD operations, searching, sorting, transaction processing, inventory management, discount systems, statistical reporting, CSV export, JSON data import, and SQLite database storage.

The project follows a **3-Layer Architecture**:

* Models Layer
* Services Layer
* Views Layer

and demonstrates all four core OOP principles:

* Encapsulation
* Inheritance
* Polymorphism
* Abstraction

---

# 2. Project Objectives

The system aims to:

* Manage library resources efficiently
* Store data permanently using SQLite
* Demonstrate OOP concepts
* Implement transaction processing logic
* Generate statistical reports
* Export reports to CSV files
* Apply discount codes automatically
* Maintain inventory stock levels

---

# 3. System Architecture

Digital-Library-Management/

├── models/        → Data Models

├── services/      → Business Logic

├── views/         → User Interface

├── database/      → SQLite & JSON Storage

├── exports/       → Generated Reports

├── README.md

└── main.py

---

# 4. Database Design

## Books Table

| Field       | Type    |
| ----------- | ------- |
| item_id     | TEXT    |
| title       | TEXT    |
| author      | TEXT    |
| book_type   | TEXT    |
| price       | REAL    |
| stock       | INTEGER |
| rental_days | INTEGER |
| file_size   | REAL    |
| duration    | INTEGER |

---

## Transactions Table

| Field            | Type    |
| ---------------- | ------- |
| transaction_id   | TEXT    |
| customer_name    | TEXT    |
| item_title       | TEXT    |
| quantity         | INTEGER |
| total_fee        | REAL    |
| transaction_date | TEXT    |

---

# 5. Technologies Used

* Python 3
* SQLite3
* JSON
* CSV
* Object-Oriented Programming (OOP)
* Git & GitHub
* Command Line Interface (CLI)

---

# 6. Project Structure

Digital-Library-Management/

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

│   ├── library.db

│   ├── books.json

│   ├── books.txt

│   ├── transactions.json

│   └── transactions.txt

│

├── README.md

└── main.py

---

# 7. Main Features

## 7.1 Book Management

✔ Add Book

✔ View All Books

✔ Search Book by ID

✔ Search Book by Title

✔ Update Book Information

✔ Update Book Details

✔ Delete Book

---

## 7.2 Book Types

### Paper Book

* Stock Management
* Rental Days

### EBook

* Stock Management
* Rental Days
* File Size

### AudioBook

* Stock Management
* Rental Days
* File Size
* Duration

---

## 7.3 Search & Sorting

* Search by Book ID
* Search by Title
* Sort by Price (Descending)

---

## 7.4 Transaction System

The transaction module supports:

* Book purchasing/renting
* Quantity validation
* Inventory checking
* Automatic stock deduction
* Discount code processing
* Transaction history storage

Supported Discount Codes:

| Code      | Discount |
| --------- | -------- |
| STUDENT10 | 10%      |
| VIP20     | 20%      |
| NONE      | 0%       |

---

## 7.5 Statistics & Reports

Generate reports including:

* Total Revenue
* Total Transactions
* Average Transaction Value
* Monthly Revenue Statistics
* Top 3 Best-Selling Books

---

## 7.6 Export Features

Export transaction reports to:

* CSV File

Example:

transactions_report.csv

---

# 8. OOP Concepts Used

## Encapsulation

Private attributes using:

```python
__stock
__price
__duration
```

with Getter/Setter validation.

---

## Inheritance

```text
LibraryItem
│
├── PaperBook
├── EBook
└── AudioBook
```

---

## Polymorphism

Each book type overrides:

```python
calculate_fee()
```

according to its own pricing logic.

---

## Abstraction

LibraryItem acts as an Abstract Base Class (ABC).

---

# 9. Menu System

```text
==================================================
DIGITAL LIBRARY MANAGEMENT SYSTEM
==================================================

1. Add Book
2. View All Books
3. Search Book by ID
4. Search Book by Title
5. Sort Books by Price (Descending)
6. Update Book Information
7. Update Book Details
8. Delete Book

----- Transactions -----

9. Create Transaction
10. View Transactions

----- Reports -----

11. View Statistics Report
12. Export CSV Report

0. Exit
```

---

# 10. Input Validation

The system validates:

* Empty IDs
* Negative prices
* Invalid quantities
* Invalid stock values
* Invalid rental days
* Invalid file sizes
* Invalid durations
* Invalid discount codes

---

# 11. Exception Handling

The application uses:

```python
try:
    ...
except Exception:
    ...
```

to prevent crashes and handle invalid user input safely.

---

# 12. Permanent Storage

The application supports:

### SQLite Database

library.db

Stores:

* Books
* Transactions

### JSON Import

books.json

transactions.json

Automatically imported when the application starts.

---

# 13. Advanced Features

### Complex Transaction Logic

* Inventory Validation
* Quantity Checking
* Discount Application
* Automatic Stock Deduction
* Revenue Calculation

### Statistical Reporting

* Revenue Statistics
* Monthly Revenue Analysis
* Best-Selling Books

### CSV Export

Export transaction data for external analysis.

### SQLite Database

Permanent database storage instead of temporary memory.

---

# 14. How to Run

Open terminal in project folder:

```bash
py main.py
```

or

```bash
python main.py
```

---

# 15. Student Information

Name: Đỗ Thanh Danh

Student ID: 24S7040004

Class: Tin 2E

Course: Programming Methods

---

# 16. Evaluation Criteria Coverage

| Requirement               | Status |
| ------------------------- | ------ |
| Encapsulation             | ✅      |
| Inheritance               | ✅      |
| Polymorphism              | ✅      |
| Abstraction               | ✅      |
| Layered Architecture      | ✅      |
| Clean Code                | ✅      |
| Exception Handling        | ✅      |
| CRUD Operations           | ✅      |
| Search & Sort             | ✅      |
| File I/O (JSON/TXT)       | ✅      |
| Complex Transaction Logic | ✅      |
| Statistics & Reports      | ✅      |
| SQLite Database           | ✅      |
| Git & GitHub              | ✅      |

---

# 17. Self Assessment

| Category             | Score   |
| -------------------- | ------- |
| OOP Design           | 1.5     |
| CRUD System          | 1.0     |
| Search & Sort        | 1.0     |
| Transaction Logic    | 1.0     |
| Reports & Statistics | 1.0     |
| SQLite Database      | 0.5     |
| GitHub Management    | 0.25    |
| Exception Handling   | 0.5     |
| File I/O             | 1.0     |
| TOTAL                | 10 / 10 |

```
```
