import time as t
from src.utils.menu import main_menu, product_menu, courier_menu, orders_menu
#from src.products.products_function import clear_console,list_product,create_products,update_products,delete_products,list_couriers, create_couriers,update_courier, delete_couriers  
from src.app_function_refac import clear_console, list_items, create_items, update_items, delete_items, create_order, update_order_status, update_order, delete_order
from file_readers.csv_to_dict_reader import csv_dict_converter


products = csv_dict_converter('./data/csv_files/products.csv')
couriers = csv_dict_converter('./data/csv_files/couriers.csv')
orders = csv_dict_converter('./data/csv_files/orders.csv')

##################################################################### create generic functions for updating/ creating and delete from dictionaries regardless of dict type (order, product, couriers) ##############################

# print(f'\t\tproducts:\n{products}\n\t\tcouriers\n{couriers}\n\t\torders\n{orders}')


# split the keys from the dictionary 
# need to index the first item in the list / we only ever need the first item to parse the keys

#product create logic 
# wrap this in a function 

# new_product_record = {'name': '', 'price':''}

# p_keys = products[0].keys()

# for key in p_keys: 
#     new_product_record[key] = input(f'please enter {key}:')

# print(new_product_record)

# # update a little more involved 

# # print out the keys

# index_key_map = {1:'name', 2:'price'}

#  a function to create the above 

# a dictionary comprehension 
# zip to lists into a dictionary 

for num, record in enumerate(products): print(num)

p_keys = products[0].keys()

