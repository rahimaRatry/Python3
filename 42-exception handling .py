# we can write multiple exception name in one except block.
try: 
    my_file = open('test.txt2') 
    content = my_file.read() 
    i = int(content.strip()) 
except (IOError, ValueError): 
    pass  
print("Error!") 
