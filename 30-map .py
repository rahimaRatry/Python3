# map is a built-in function.we need to take 2 arguments here, first one is Function and second one is Iterator Object.

my_list = [2, 3, 4, 5, 6, 7] # Iterator Object
def square(x) :  #Function
    return x * x
new_list = map(square, my_list) 
print(new_list) 
print(list(new_list)) 
