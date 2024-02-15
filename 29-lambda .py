# by using lambda operator we can write one single line funtion in python.

sum = lambda a, b : a + b
print(sum(10,20))
print((lambda a, b : a + b)(10, 20)) 

#anonymous function
def my_function(func, arg1, arg2):
    return func(arg1, arg2)
print(my_function(lambda a, b : a + b, 10, 20)) 