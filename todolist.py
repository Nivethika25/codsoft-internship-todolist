todo_list = []

# Function to add an item to the todo list
def add_item():
    item = input("Enter the item to add: ")
    todo_list.append(item)
    print(f"Item '{item}' added to the todo list.")

# Function to remove an item from the todo list
def remove_item():
    item = input("Enter the item to remove: ")
    if item in todo_list:
        todo_list.remove(item)
        print(f"Item '{item}' removed from the todo list.")
    else:
        print("Item not found in the todo list.")

# Function to display the todo list
def display_list():
    if todo_list:
        print("Todo List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Todo list is empty.")

# Main function to run the todo list program
def main():
    while True:
        print("\n===== Todo List Menu =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            display_list()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
