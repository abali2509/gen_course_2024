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


#def get_enumerated_list(list:list):

    for num, value in enumerate(list):

        print(f'{num}: {value}')



def create_order(orders_list: list, couriers_list:list)->dict:

    # another funtion that read the csv orders list 



    order = {'customer_name':'','customer_address':'','customer_phone':'','courier':'','status':'Preparing'}

    order['customer_name'] = str(input(f'Please state your name: '))
    order['customer_address'] = str(input('Please state your address: '))
    order['customer_phone'] = str(input('Please state your phone number: '))

    # call courier list function or function that list csv file 

    list_items(couriers_list)

    # use the couriers_list to print enumatered list 

    order['courier'] = int(input('Please state the courier you want to assign the order to: '))

    orders_list.append(order)

    return orders_list


def update_order_status(orders_list):

    #Here we are taking in the list of dictionaries, and spitting it back out with index values beside each order
    list_items(orders_list)

    #We are requesting the user to select an order to edit
    order_index = int(input('Please select which order you would like to update?'))-1

    #We need to create a list of order status options for the user to choose from
    order_status = ['Preparing', 'Prepared', 'Out for Delivery', 'Delivered']

    #Again call the list_items function which creates an index value next to each status option 
    list_items(order_status)

    #Give the user the opporuntity to select a status from the list 
    selcted_status = int(input('Please select a status'))-1

    #Retrive the selected status
    chosen_status = order_status[selcted_status]

    #Now were upadating the indexed order we specificed early with the new status we have selected
    orders_list[order_index]['status'] = chosen_status



def update_order(orders_list):

    #List dictionary item with index
    list_items(orders_list)

    #Select which index you want to edit
    index_order = int(input('Please select which order you would like to update?'))


    #Run a for loop which will allow the option to access the key, value pairs of the dictionary so for each name, address etc...
    for k, v in orders_list[index_order].items():

        #Print the key, value pair so you know which one your currently in
        print(f' This is the current key value pair we are in {k} : {v}')
       
       #Now were giving the user the option to edit the value given the current key we are in. Otherwise press enter and it will quit
        change_input = input(f'what value do you want to change the {k} value, otherwise if you want to keep the same press enter')

        #If the user pressess enter it will break out of the loop
        if change_input == "":
            break

        #Otherwise the user can now take the changed value for the key, and replace the old value with the new
        else:
            orders_list[index_order][k] = change_input


def delete_order(orders_list):

    list_items(orders_list)
        
    index_order = int(input('Please select which order you would like to update?'))

    del orders_list[index_order]