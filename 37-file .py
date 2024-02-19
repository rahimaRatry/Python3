
my_file = open('test.txt','r') 
content = my_file.read(5) # here we passed 5 so firstly it will read first five characters including space.
print(content) 
content = my_file.read() 
print(content) 
position = my_file.tell() #by using tell() we found the position of file pointer. 
print(position) 
my_file.seek(0, 0) # by using seek() we took that file pointer in the begining.
content = my_file.read() 
print(content) 
my_file.close() 
