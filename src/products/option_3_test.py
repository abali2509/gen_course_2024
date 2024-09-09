'''def get_enumerated_list(list:list):

    for num, value in enumerate(list):

        print(f'{num}: {value}')


data = [
    {
        "name": "Alice",
        "age": 28,
        "city": "New York"
    },
    {
        "name": "Bob",
        "age": 34,
        "city": "Los Angeles"
    },
    {
        "name": "Charlie",
        "age": 22,
        "city": "Chicago"
    }
]


def get_enumerated_list(data):
    for index, item in enumerate(data):
        print(f"{index}: {item['name']}, {item['age']}, {item['city']}")

# Display the enumerated list
get_enumerated_list(data)

# Get the user's selection by index
chosen_index = int(input('Please select the index you want: '))

# Access the chosen dictionary
if 0 <= chosen_index < len(data):
    chosen_item = data[chosen_index]
    print(f"You selected: {chosen_item}")
else:
    print("Invalid index")


order_age = int(input('Please state what you want the status of the order to be'))

chosen_item['age'] = order_age

print(chosen_item)
'''

import csv


def csv_dict_converter(file_path:str):
    with open(file_path, 'r') as file:

        dict_reader = csv.DictReader(file)

        list_of_dict = list(dict_reader)

        print(list_of_dict)

orders = csv_dict_converter('data/csv_files/orders.csv')

print(orders)


def get_enumerated_list(orders):
    for index, order in enumerate(orders):
        print(f'{index}:, {order['customer_name']}, {order['customer_address']}, {order['customer_phone']}, {order['courier']}, {order['status']}')


get_enumerated_list(orders)

chosen_index = int(input('Please state which order you will like to select'))

if 0 <= chosen_index < len(orders):
    chosen_item = data[chosen_index]
else:
    print('Please provide a valid index')

order_status = input('Please state what you will like the order status to be')

chosen_index['status'] = order_status
                   

                   


""""
get_enumerated_list(data)

chosen_index = int(input('Please selected the index you want '))

specicied_index =orders_indexed_list[chosen_index]
print(specicied_index)

"""









'''''
indexed_Num =Which index value do you want to pick out 

	chosen_order = orders_indexed_number

	print(chosen_order[‘status’])

	change_order_status = input(‘Please change order status’)

	chosen_order[‘status’] = changed_order_status



    '''

