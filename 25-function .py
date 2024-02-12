# Variable length argument
def add(*args):   #here we've to use * which means this argument can hold unlimited value
    print(type(args))
    tmp = 0
    for number in args:
        tmp = tmp+number
    return tmp
temp = add(1,2,22,12,17,21,98,100)
print(temp) 

# keyworded variable lenth argument
def add(**kwargs):   #To pass keyword arguments we need to write two ** before the parameter
    print(type(kwargs))
    tmp = 0
    for key in kwargs:
        tmp = tmp+kwargs[key]
    return tmp 
temp = add(a=1, b=2, c=3, d=4)
print(temp) 