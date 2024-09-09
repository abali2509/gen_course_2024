import time as t
from src.utils.menu import main_menu, product_menu, courier_menu
#from src.products.products_function import clear_console,list_product,create_products,update_products,delete_products,list_couriers, create_couriers,update_courier, delete_couriers  
from src.app_function_refac import clear_console, list_items, create_items, update_items, delete_items, create_order, update_order_status, update_order, delete_order

from file_readers.reader_test import open_file, write_anything
from file_readers.csv_to_dict_reader import csv_dict_converter


#products = open_file('./data/txt_files/products.txt')
#couriers = open_file('./data/txt_files/couriers.txt')

orders = csv_dict_converter('./data/csv_files/orders.csv')


# Main loop
while True:
    clear_console()  # Clear the console before showing the main menu
    print(main_menu)

    

    try:
        main_menu_option = int(input('Please select an option:\n'))

        if main_menu_option == 1:

            
            while True:
                clear_console()  # Clear the console before showing the product menu
                print(product_menu)

                try:
                    product_menu_option = int(input('Please select an option:\n'))

                    if product_menu_option == 1:
                        clear_console()
                        list_items(item_list=products)
                        input("Press Enter to continue...")  

                    
                    elif product_menu_option == 2:
                        clear_console()
                        create_items(item_list=products)
                        input("Press Enter to continue...")

                    elif product_menu_option == 3:
                        clear_console()
                        update_items(item_list=products)
                        input("Press Enter to continue...")

                    elif product_menu_option == 4:
                        clear_console()
                        delete_items(item_list=products)
                        input("Press Enter to continue...")

                    elif product_menu_option == 0:
                        break
                    else:
                        print("Please select a valid option.")
                        t.sleep(1)  # Wait for a moment before clearing the console
            
            

                except ValueError:
                    print("Please enter a valid number.")
                    t.sleep(1)  # Pause to let the user see the error before clearing the console
            
            write_anything(products,'./data/txt_files/products.txt')

        elif main_menu_option == 2:
            while True:
                clear_console()  # Clear the console before showing the product menu
                print(courier_menu)

                try:
                    courier_menu_option = int(input('Please select an option:\n'))

                    if courier_menu_option == 1:
                        clear_console()
                        list_items(item_list=couriers)
                        input("Press Enter to continue...")  # Pause so the user can see the list before clearing again

                    elif courier_menu_option == 2:
                        clear_console()
                        create_items(item_list=couriers)
                        input("Press Enter to continue...")

                    elif courier_menu_option == 3:
                        clear_console()
                        update_items(item_list=couriers)
                        input("Press Enter to continue...")

                    elif courier_menu_option == 4:
                        clear_console()
                        delete_items(item_list=couriers)
                        input("Press Enter to continue...")

                    elif courier_menu_option == 0:
                        break
                    else:
                        print("Please select a valid option.")
                        t.sleep(1)  # Wait for a moment before clearing the console
                
                except ValueError:
                    print("Please enter a valid number.")
                    t.sleep(1)  # Pause to let the user see the error before clearing the console

            write_anything(couriers, './data/txt_files/couriers.txt')

        elif main_menu_option == 3:
            while True:
                clear_console()  # Clear the console before showing the product menu
                print(orders_menu)



                if orders_menu_option == 1:
                    clear_console()
                    list_items(items_list = orders)
                    
                
                elif orders_menu_option == 2:
                    clear_console()
                    create_order(orders, couriers)

                    

                elif orders_menu_option == 3:
                    clear_console()
                    update_order_status(orders)



                elif order_menu_option == 4:
                    clear_console()
                    update_order(orders)


                elif order_menu_option == 5:
                    clear_console()
                    delete_order(orders)

                elif product_menu_option == 0:
                            break




            elif main_menu_option == 0:
        
                print("Exiting the program...")
                break 
        else:
            print("Please select a valid option.")
            t.sleep(1)  # Pause to let the user see the message before clearing the console
    except ValueError:
        print("Please enter a valid number.")
        t.sleep(1)  # Pause to let the user see the error before clearing the console
