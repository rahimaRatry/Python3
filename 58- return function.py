# we can also return the function as well. 

def get_int_as_str(number): 
    print(str(number)) 
    return 
def print_int(my_function, number): 
    return my_function(number) 
print_int(get_int_as_str, 130) 

# or we can define "get_int_as_str()" function in "print_int()" function--- 

def print_int(number):

    def get_int_as_str(number):
        print(str(number)) 
        return
     
    get_int_as_str(number) 
    return 

print(130) 


# And also we can write like this--

def print_int(number): 

    def get_int_as_str(number):
        print(str(number)) 
        return
    
    return get_int_as_str(number)  

print_int(130) 
