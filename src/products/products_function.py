import os 
# Function to clear the console based on the operating system

def clear_console():
    os.system('clear')

# Products lists - to be used in product related activates 
products = ['Americano', 'Latte', 'Green Tea', 'English Tea', 'Water']

couriers = ['John', 'Jacob',  'Desmond', 'Lucy']

# Function to list products
def list_product(product_list: list) -> None:
    """
    Prints enumerated list of products.
    Parameter:
    product_list - list of products
    """
    for num, product in enumerate(product_list, 1):
        print(f'{num}. {product}')

# Function to append multiple new products to the product list
def create_products(product_list: list) -> None:
    """
    Appends new products to list of products.
    Parameter:
    product_list - list of products 
    """
    number_of_products = int(input('How many products do you want to create?\n'))
    while number_of_products > 0:
        new_product = input('Please enter the name of the new product:\n')
        if new_product not in product_list:
            product_list.append(new_product)
            print(f'{new_product} has been added to the product list.')
        else: 
            print(f'{new_product} already exists in the product list.')
        number_of_products -= 1

# Function to update multiple products in the product list
def update_products(product_list: list) -> None:
    """
    Allows the user to update multiple products in the product list.
    Parameter:
    product_list - list of products 
    """
    while True:
        list_product(product_list)
        try:
            product_index = int(input('Please enter the number of the product you want to update (or enter 0 to finish):\n')) - 1
            if product_index == -1:
                print("Exiting update mode.")
                break
            if 0 <= product_index < len(product_list):
                product_update = input('Please enter the new product name:\n')
                product_list[product_index] = product_update
                print(f'Product at position {product_index + 1} has been updated to {product_update}.')
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete multiple products from the product list
def delete_products(product_list: list) -> None:
    """
    Allows the user to delete multiple products from the product list.
    Parameter:
    product_list - list of products 
    """
    while True:
        list_product(product_list)
        try:
            product_index = int(input('Please enter the number of the product you want to delete (or enter 0 to finish):\n')) - 1
            if product_index == -1:
                print("Exiting delete mode.")
                break
            if 0 <= product_index < len(product_list):
                deleted_product = product_list.pop(product_index)
                print(f'{deleted_product} has been deleted from the product list.')
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter a valid number.")








# Function to list couriers
def list_couriers(courier_list: list) -> None:
    """
    Prints enumerated list of products.
    Parameter:
    courier_list - list of products
    """
    for num, courier in enumerate(courier_list, 1):
        print(f'{num}. {courier}')

# Function to append multiple new courier to the courier list
def create_couriers(courier_list: list) -> None:
    """
    Appends new products to list of courier.
    Parameter:
    courier_list - list of products 
    """
    number_of_courier = int(input('How many courier do you want to create?\n'))
    while number_of_courier> 0:
        new_courier = input('Please enter the name of the new courier:\n')
        if new_courier not in courier_list:
            courier_list.append(new_courier)
            print(f'{new_courier} has been added to the courier list.')
        else: 
            print(f'{new_courier} already exists in the courier list.')
        number_of_courier -= 1

# Function to update multiple courier in the courier list
def update_courier(courier_list: list) -> None:
    """
    Allows the user to update multiple courier in the courier list.
    Parameter:
    courier_list - list of courier 
    """
    while True:
        list_couriers(courier_list)
        try:
            courier_index = int(input('Please enter the number of the courier you want to update (or enter 0 to finish):\n')) - 1
            if courier_index == -1:
                print("Exiting update mode.")
                break
            if 0 <= courier_index < len(courier_list):
                courier_update = input('Please enter the new courier name:\n')
                courier_list[courier_index] = courier_update
                print(f'Courier at position {courier_index + 1} has been updated to {courier_update}.')
            else:
                print("Invalid courier number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete multiple products from the product list
def delete_couriers(courier_list: list) -> None:
    """
    Allows the user to delete multiple courier from the couriers list.
    Parameter:
    courier_list - list of couriers 
    """
    while True:
        list_couriers(courier_list)
        try:
            courier_index = int(input('Please enter the number of couriers you want to delete (or enter 0 to finish):\n')) - 1
            if courier_index == -1:
                print("Exiting delete mode.")
                break
            if 0 <= courier_index < len(courier_list):
                deleted_courier = courier_list.pop(courier_index)
                print(f'{deleted_courier} has been deleted from the courier list.')
            else:
                print("Invalid courier number.")
        except ValueError:
            print("Please enter a valid number.")
