#Below is the products_fucntion refactored to be able to take both products & couriers arguments

import os

# Function to clear the console based on the operating system
def clear_console():
    os.system('clear')

# Generic function to list items
def list_items(item_list: list) -> None:
    """
    Prints enumerated list of items (e.g., products, couriers).
    """
    print("\nList of Items:")
    for num, item in enumerate(item_list, 1):
        print(f'{num}. {item}')
    

# Generic function to append new items to a list
def create_items(item_list: list) -> None:
    """
    Appends new items to a list (e.g., products, couriers).
    """
    number_of_items = int(input('How many items do you want to create?\n'))
    while number_of_items > 0:
        new_item = input('Please enter the name of the new item:\n')
        if new_item not in item_list:
            item_list.append(new_item)
            print(f'{new_item} has been added to the list.')
        else:
            print(f'{new_item} already exists in the list.')
        number_of_items -= 1

# Generic function to update items in a list
def update_items(item_list: list) -> None:
    """
    Allows the user to update items in a list (e.g., products, couriers).
    """
    list_items(item_list)
    while True:
        try:
            item_index = int(input('Please enter the number of the item you want to update (or enter 0 to finish):\n')) - 1
            if item_index == -1:
                print("Exiting update mode.")
                break
            if 0 <= item_index < len(item_list):
                new_name = input('Please enter the new item name:\n')
                item_list[item_index] = new_name
                print(f'Item at position {item_index + 1} has been updated to {new_name}.')
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

# Generic function to delete items from a list
def delete_items(item_list: list) -> None:
    """
    Allows the user to delete items from a list (e.g., products, couriers).
    """
    list_items(item_list)
    while True:
        try:
            item_index = int(input('Please enter the number of the item you want to delete (or enter 0 to finish):\n')) - 1
            if item_index == -1:
                print("Exiting delete mode.")
                break
            if 0 <= item_index < len(item_list):
                deleted_item = item_list.pop(item_index)
                print(f'{deleted_item} has been deleted from the list.')
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")