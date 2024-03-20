# try-except-finally.finally block will must execute.It doesn't matter if there is any error found or not.

try: 
    with open('test.txt2','r') as my_file: 
        content = my_file.read() 
        print(content) 
except FileNotFoundError: 
    print("The file does not exist.") 
finally: 
    print("To be or not to be that is the Question.")  