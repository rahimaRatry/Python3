"""To open a file we use 'open()' function, it works with 3 parameters- file name, access mode and buffering."""

my_file = open('test.txt1', 'r')  #'r' used to open the file in read mode.
content = my_file.read()   #by using 'read()' method, we read the data and assigned that into content variable. 
print(content) 
my_file.close()   #'close()' used to close the file.