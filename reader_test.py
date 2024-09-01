# read 
def open_file(path:str)-> list:

    file = open(path, "+r")
    
    file_contents = []

    for line in file.readlines():
        file_contents.append(line.rstrip())
    file.close()
    return file_contents
    

# write 

def write_anything(file_contents: list, path: str)-> None:
    
    with open(path, "r+") as file:
        for l in file_contents:
            file.write(f'{l}\n')
        # file.write('Hello')

    
    
    


products = open_file("./data/txt_files/products.txt")
products.remove('Water')
write_anything(products, "./data/txt_files/products.txt")
# for product in products:
#     print(product)
# # openning a file
# products = open("./data/txt_files/products.txt", "+r")

# print(type(products))
# # reading the content
# contents = products.read()

# # printing content 
# print(contents)



# # close file 
# products.close()






