


import csv


def csv_dict_converter(file_path:str):
    with open(file_path, 'r') as file:

        dict_reader = csv.DictReader(file)

        list_of_dict = list(dict_reader)

        print(list_of_dict)