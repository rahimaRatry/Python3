# we can declare multiple except block for one try block.

try: 
    my_file = open('test.txt2') 
    content = my_file.read() 
    i = int(content.strip()) 

except IOError as e: 
    errno, strerror = e.args 
    print("I/O error({0}): {1}".format(errno,strerror)) 

except ValueError: 
    print("No valid integer in line.") 

except:   # It is called Bare Except. we should avoid this because it will hide all type of error.
    print("Unexpected Error!")  # and we won't able to know the exact error. 
