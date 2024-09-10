import csv


def csv_dict_converter(file_path:str):

    with open(file_path, 'r') as file:

        dict_reader = csv.DictReader(file, delimiter='|')

        list_of_dict = list(dict_reader)

        return list_of_dict