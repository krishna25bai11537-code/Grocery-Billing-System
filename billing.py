# Grocery Store Billing System

items = []
prices = []

print("Enter items and their prices for your bill.")
number_of_items = int(input("How many items do you want to enter? "))

for _ in range(number_of_items):
    item = input("Enter item name: ")
    price = input(f"Enter price for {item}: ")
    try:
        price = float(price)
    except ValueError:
        print("Invalid price. Please enter a number.")
        price = float(input(f"Enter price for {item} again: "))
    items.append(item)
    prices.append(price)

print("\n----- BILL RECEIPT -----")
total = 0
for i in range(len(items)):
    print(f"{items[i]}: ₹{prices[i]:.2f}")
    total += prices[i]
print("------------------------")
print(f"TOTAL BILL AMOUNT: ₹{total:.2f}")
