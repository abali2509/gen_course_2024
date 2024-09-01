# read 
def open_file(path:str)-> list:

    file = open(path, "+r")
    
    file_contents = []

    for line in file.readlines():
        file_contents.append(line.rstrip())

    return file_contents
    

# write 




products = open_file("./data/txt_files/products.txt")

print(products)
# # openning a file
# products = open("./data/txt_files/products.txt", "+r")

# print(type(products))
# # reading the content
# contents = products.read()

# # printing content 
# print(contents)



# # close file 
# products.close()






