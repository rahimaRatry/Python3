""" In 'try' block, we write the general code. when an exception will raise then the 'exception' block will 
execute."""

try: 
    with open('txt.test2','r') as my_file: 
        content = my_file.read() 
        print(content) 
except: 
    print("The file does not exist.") 
print("Made by Ratry") 