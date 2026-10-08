#create an empty list
#give option to user to
#add item
#remove item
#view list
#sort list
#quit
#Don't add duplicates (check case-insensitively).
#Print a friendly message when the user tries to remove an item that isn't on the list.
#Show the list numbered from 1.

items = []

while True:
    print("--- MENU ---")
    print("Choose 1 to Add item")
    print("Choose 2 to Remove item")
    print("Choose 3 to View list")
    print("Choose 4 to Sort list")
    print("Choose 5 to Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        if item.lower() in [x.lower() for x in items]:       # Check for duplicates (case-insensitive)
            print("That item is already in the list.")
        else:
            items.append(item)
            print("Item added successfully.")

    elif choice == "2":
        item = input("Enter item to remove: ")

        # Find the actual item ignoring case
        found = None
        for x in items:
            if x.lower() == item.lower():
                found = x
                break

        if found:
            items.remove(found)
            print("Item removed successfully.")
        else:
            print("Sorry, that item isn't in the list.")

    elif choice == "3":
        if len(items) == 0:
            print("The list is empty.")
        else:
            print("Your list:")
            for number, item in enumerate(items, start=1):
                print(number, ".", item)

    elif choice == "4":
        items.sort(key=str.lower)
        print("List sorted successfully.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-5.")
