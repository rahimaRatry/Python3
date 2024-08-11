# function is a first class object.So that we can pass the function like  normal value or variable, and we
# can use functions as parameter or argument.

def get_int_as_str(number): 
    return str(number) 

def print_int(my_function, number): 
    print(my_function(number)) 
    return 

print_int(get_int_as_str, 130) 
