# 🎯 Project Statement: Grocery Store Billing System

---

## 📝 Problem Statement

Currently, small grocery stores, vendors, and home businesses often rely on **manual calculation** or generic calculator applications to tally customer purchases. This process is prone to **human errors** (miscalculation, data entry mistakes) and lacks **transparency** for the customer, as it does not provide a formal, itemized receipt detailing applied discounts or taxes. This inefficiency results in time loss and potential revenue leakage.

---

## 🗺️ Scope of the Project

The primary scope of this project is to develop a **command-line interface (CLI) application** that automates the bill generation process for a single customer transaction.

### In Scope
* **Itemized Entry:** Recording item names and prices.
* **Total Calculation:** Calculating the subtotal.
* **Fixed Rate Application:** Applying hardcoded, configurable constants for **Discount Rate** and **Tax Rate**.
* **Receipt Output:** Generating a clean, detailed, itemized receipt in the console.
* **Robust Input Validation:** Ensuring only valid, positive numeric data is accepted for prices.

### Out of Scope (Future Enhancements)
* Database integration (e.g., storing past transactions or inventory).
* Handling item quantity (currently fixed at 1 unit per entry).
* User interface (GUI or web-based interface).
* Payment processing or tender management.

---

## 👤 Target Users

The system is designed for individuals or small businesses needing a quick, reliable way to calculate sales transactions.

* **Small Grocery Store Owners/Cashiers:** To speed up checkout and minimize manual errors.
* **Small Scale Vendors:** Individuals selling goods at markets or temporary stalls.
* **Home Businesses/Entrepreneurs:** For managing sales of small-volume, high-value items (e.g., homemade crafts, baked goods).
* **Students/Beginners:** For learning fundamental programming concepts like data structures, input/output, and basic arithmetic operations in a practical context.

---

## ✨ High-Level Features

1.  **Guided Data Entry:** Provides clear prompts for the user to input the name and price of each item being purchased.
2.  **Price Integrity Check:** Implements error handling to ensure prices are valid numeric figures before being added to the bill.
3.  **Subtotal Calculation:** Automatically calculates the sum of all item prices entered.
4.  **Discount & Tax Application:** Applies predefined percentage rates for discounts and sales tax to the subtotal.
5.  **Final Transaction Summary:** Presents the customer with a complete, detailed breakdown of the item-wise list, subtotal, adjustments, and the final amount due.
