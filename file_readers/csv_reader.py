
import csv

def read_csv(file_path: str) -> None:

    with open(file_path, newline='') as csv_file:

        reader = csv.reader(csv_file)

        for file in reader:
            print(file)


products_csv = ("./data/csv_files/products.csv")


read_csv(products_csv)

