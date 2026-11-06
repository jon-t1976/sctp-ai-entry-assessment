# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

# Add your code here
inventory = []


# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."

def addItem(itemName):
    # Add your code here

# Check if the item is already present in the inventory list
    if itemName in inventory:
        # Print a warning message using an f-string for the specific item
        print(f"{itemName} is already in inventory.")
    else:
        # If not present, append the new item to the list
        inventory.append(itemName)



# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."

def listInventory():
# Check if the list has no elements
    if len(inventory) == 0:
        # Print the message "Inventory is empty." if the list has no elements
        print("Inventory is empty.")
    else:
        # Print the entire list matching the expected output format
        print(f"Inventory: {inventory}")


# Task 4:
# Call the functions in this order and observe the output:
addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
