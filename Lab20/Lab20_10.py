# Store item names with their price and quantity
# Create an empty cart
# Keep asking the customer for items
# Ask the customer to enter an item and quantity
# Stop taking orders if the customer enters done
# Split the input into item and quantity
# Check that exactly two values were entered
# Store the item name
# Check if the item exists in the inventory
# Try to convert the quantity into a number
# Check that the quantity is positive
# Get the price and available stock
# Check if there is enough stock
# Add the item to the cart
# Reduce the inventory stock
    # since tuples cannot be changed, so create a new tuple
# Confirm the order
# Print the receipt heading
# Print the column headings
# Create a variable to store the subtotal
# Go through every item in the cart
# Get the price from the inventory
# Calculate the total for this item
# Add the line total to the subtotal
# Print the item details in aligned columns
# Print a line
# Check if the subtotal is greater than ₹500
# Calculate 10% discount
# No discount
# Calculate the final amount
# Print subtotal
# Print discount
# Print final tota
# Print the updated inventory
# Go through every item in the inventory
# Check if fewer than 10 items are left
# Print the updated item information

inventory = {
    "pen": (10.0, 50),
    "notebook": (45.0, 20),
    "eraser": (5.0, 100),
    "marker": (30.0, 15)
}

cart = {}
while True:
    entry = input("Enter item and quantity (example: pen 3) or 'done': ")
    if entry.lower() == "done":
        break

    parts = entry.split()
    if len(parts) != 2:
        print("Please enter an item and quantity, for example: pen 3")
        continue

    item = parts[0].lower()
    if item not in inventory:
        print("Unknown item.")
        continue

    try:
        quantity = int(parts[1])
    except ValueError:
        print("Quantity must be a valid number.")
        continue

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    price, stock = inventory[item]

    if quantity > stock:
        print("Not enough stock available.")
        continue
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity

    inventory[item] = price, stock-quantity

    print("Item added to cart.")

print("\n" + "=" * 55)
print("RECEIPT")
print("=" * 55)

print(
    "Item".ljust(15),
    "Qty".rjust(5),
    "Unit Price".rjust(12),
    "Line Total".rjust(15)
)

print("-" * 55)

subtotal = 0

for item, quantity in cart.items():
    price, stock = inventory[item]
    line_total = price * quantity
    subtotal += line_total

    print(
        item.ljust(15),
        str(quantity).rjust(5),
        f"₹{price:.2f}".rjust(12),
        f"₹{line_total:.2f}".rjust(15)
    )
print("-" * 55)
if subtotal > 500:
    discount = subtotal * 0.10

else:
    discount=0
total = subtotal - discount

print(f"{'Subtotal:'.ljust(20)} ₹{subtotal:.2f}")

print(f"{'Discount:'.ljust(20)} ₹{discount:.2f}")

print(f"{'Total:'.ljust(20)} ₹{total:.2f}")

print("=" * 55)
print("UPDATED INVENTORY")
print("=" * 40)

for item, (price, stock) in inventory.items():
    if stock < 10:
        status = "LOW STOCK"
    else:
        status = ""

    print(
        f"{item.ljust(12)} "
        f"Price: ₹{price:.2f} "
        f"Stock: {str(stock).rjust(3)} "
        f"{status}"
    )

