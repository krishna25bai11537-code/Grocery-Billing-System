# Grocery-Billing-System
Vityarthi Project
# 🛒 Grocery Store Billing System

---

## 💡 Overview

This project is a simple, command-line based **Grocery Store Billing System** built using Python. It allows a cashier or user to enter items and their corresponding prices, calculates the subtotal, applies a predefined discount and tax rate, and displays a detailed final receipt. It features **robust input validation** to ensure that only valid numeric prices are accepted.

---

## ✨ Features

* **Interactive Input:** Prompts the user for the number of items and their details.
* **Robust Error Handling:** Utilizes a `while` loop with `try-except` blocks to ensure prices are valid numbers greater than zero.
* **Detailed Receipt Generation:** Prints a clear breakdown of the subtotal, discount, tax, and final amount due.
* **Configurable Rates:** Easily adjust the **Tax Rate** and **Discount Rate** constants within the script.
* **Clean Data Structure:** Uses a Python dictionary (`bill = {item: price}`) for efficient and logical data storage.

---

## 🛠️ Technologies / Tools Used

* **Language:** Python 3.x
* **Environment:** Command Line Interface (CLI)

---

## ⚙️ Steps to Install & Run the Project

### Prerequisites

You must have **Python 3** installed on your system.

### Installation and Execution

1.  **Clone the repository** (or save the code above as a file named `billing_system.py`).

    ```bash
    git clone [https://github.com/YourUsername/repository-name.git](https://github.com/YourUsername/repository-name.git)
    cd repository-name
    ```

2.  **Run the Python script** from your terminal:

    ```bash
    python billing_system.py
    ```

3.  The program will start by asking you to input the number of items. Follow the on-screen prompts to enter the item names and prices.

---

## ✅ Instructions for Testing

To ensure the system works correctly, test the following scenarios:

| Test Case | Expected Input | Expected Outcome |
| :--- | :--- | :--- |
| **Normal Calculation** | 2 items: Apple (10.00), Bread (15.50) | Subtotal: 25.50. Total includes 10% discount and 5% tax. |
| **Non-Numeric Price** | Item: Milk. Price: `abc` | The system prompts the user to **re-enter** a valid numeric price. |
| **Negative/Zero Price** | Item: Soda. Price: `-5.00` or `0` | The system prompts the user to enter a price **greater than zero**. |
