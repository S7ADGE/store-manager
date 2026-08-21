# 🏪 Store Manager

### A lightweight Python-based store management & invoice system.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/S7ADGE/store-manager?style=flat\&logo=github)](https://github.com/S7ADGE/store-manager)
[![GitHub Forks](https://img.shields.io/github/forks/S7ADGE/store-manager?style=flat\&logo=github)](https://github.com/S7ADGE/store-manager)

> **Store Manager** is a simple command-line application written in Python for managing customers, store items, shopping carts, invoices, and sales summaries.

---

## ✨ Features

### 👤 Customer Management

* Register customers with a unique ID
* Store customer name and family name
* Prevent duplicate customer IDs
* Support multiple customers in a single session

### 📦 Inventory Management

* Add available store items
* Assign prices to products
* Prevent duplicate items
* Display available products and their prices

### 🛒 Shopping Cart

* Select products from the store
* Set the quantity of each product
* Prevent duplicate products inside a cart
* Automatically detect when all available products have been selected

### 🧾 Invoice Generation

* Generate an invoice for each customer
* Display customer information
* Display purchased products
* Calculate quantity × unit price automatically
* Calculate the total number of purchased units
* Calculate the total cost

### 📊 Sales Summary

* Keep track of item sales
* Calculate total sales per product
* Display a final sales summary after processing customers

---

## 🧠 What This Project Demonstrates

This project was built to practice core Python programming concepts such as:

* Functions
* Loops
* Conditional statements
* Dictionaries
* Lists
* Input validation
* Exception handling
* Data processing
* Function composition
* Basic inventory logic
* Invoice and sales calculations

The project also focuses on building reusable input-validation functions and organizing a complete workflow from **customer registration → product selection → invoice generation → sales analysis**.

---

## 🔄 Application Flow

```text
                ┌─────────────────────┐
                │     Store Setup     │
                │  Add Items + Prices  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Customer Registration│
                │   ID + Name + Family │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Product Select   │
                │   Build Shopping Cart│
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │  Invoice Generation │
                │ Quantity × Price     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Sales Summary    │
                │ Total Units / Sales │
                └─────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology             | Purpose                           |
| ---------------------- | --------------------------------- |
| 🐍 Python              | Core programming language         |
| 📋 Lists               | Customer, cart and sales data     |
| 🗂️ Dictionaries       | Products, prices and invoice data |
| 🔁 Loops               | Repeated user interaction         |
| 🛡️ Exception Handling | Input validation                  |
| 🧩 Functions           | Modular application logic         |

---

## 📁 Project Structure

```text
store-manager/
│
├── src/
│   └── main.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

The main application logic is located in:

```text
src/main.py
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/S7ADGE/store-manager.git
```

### 2. Enter the project directory

```bash
cd store-manager
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python src/main.py
```

---

## 💻 Example Workflow

The application starts by asking you to define the products available in your store:

```text
Enter the item available in your store : Laptop
Enter the price of the item ($) : 850

Continue for item ? (y | n) : y

Enter the item available in your store : Mouse
Enter the price of the item ($) : 25

Continue for item ? (y | n) : n
```

Then a customer can be registered and products can be added to their cart.

The system calculates each line total using:

```text
Line Total = Quantity × Unit Price
```

and finally produces a sales summary for the processed customers.

---

## 🧮 Example Calculation

If a customer purchases:

```text
Laptop   × 2   ×   $850
Mouse    × 3   ×   $25
```

The invoice calculates:

```text
Laptop:  2 × $850 = $1700
Mouse:   3 × $25  = $75
────────────────────────
Total:                $1775
```

---

## 🎯 Project Goals

The main goal of this project is to build a practical Python application while strengthening fundamental programming skills.

The project focuses on transforming individual programming concepts into a complete workflow:

```text
Input
  ↓
Validation
  ↓
Data Storage
  ↓
Processing
  ↓
Invoice Generation
  ↓
Sales Analysis
```

---

## 🗺️ Future Improvements

Possible future versions of the project could include:

* [ ] Persistent database storage
* [ ] Product stock tracking
* [ ] Product categories
* [ ] Product search
* [ ] Customer purchase history
* [ ] Discounts and taxes
* [ ] Invoice export to PDF
* [ ] Graphical user interface
* [ ] Better reporting and analytics
* [ ] User authentication
* [ ] SQLite / PostgreSQL integration
* [ ] Automated testing

---

## 🤝 Contributing

Contributions, ideas, and improvements are welcome.

If you find a bug or have an idea for improving the project, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

## 👨‍💻 Author

**S7ADGE**

GitHub: [@S7ADGE](https://github.com/S7ADGE)

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Built with Python 🐍**

</div>
