
with open('test.txt','r') as my_file: 
    content = my_file.read() 
    print(content) 

# Here we don't need to close this file because in using of 'with' statement the file will automatically closed
# after doing it's work or if is there any error found.