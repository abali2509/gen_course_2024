import time as t
from src.utils.menu import main_menu, product_menu
from src.products.products_function import clear_console,list_product,create_products,update_products,delete_products, products


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
                        list_product(product_list=products)
                        input("Press Enter to continue...")  # Pause so the user can see the list before clearing again

                    elif product_menu_option == 2:
                        clear_console()
                        create_products(product_list=products)
                        input("Press Enter to continue...")

                    elif product_menu_option == 3:
                        clear_console()
                        update_products(product_list=products)
                        input("Press Enter to continue...")

                    elif product_menu_option == 4:
                        clear_console()
                        delete_products(product_list=products)
                        input("Press Enter to continue...")

                    elif product_menu_option == 0:
                        break
                    else:
                        print("Please select a valid option.")
                        t.sleep(1)  # Wait for a moment before clearing the console
                except ValueError:
                    print("Please enter a valid number.")
                    t.sleep(1)  # Pause to let the user see the error before clearing the console

        elif main_menu_option == 0:
            print("Exiting the program...")
            break 
        else:
            print("Please select a valid option.")
            t.sleep(1)  # Pause to let the user see the message before clearing the console
    except ValueError:
        print("Please enter a valid number.")
        t.sleep(1)  # Pause to let the user see the error before clearing the console
