
try: 
    with open('test.txt2','r') as my_file: 
        content = my_file.read() 
        print(content) 
except FileNotFoundError:   # if we know the exact error name then we can write that here.
    print("The file does not exist.") 
print("Made by Ratry.") 

try: 
    my_list = [] 
    print(my_list[0]) 
except IndexError as e: 
    print(e) # we can also print the error name.
    