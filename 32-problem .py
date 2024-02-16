"""" Take an input from the user and check if that is a Prime number or Composite number
We know if a number cannot divided with any number,but can divided by 1 and that number,
then the number is Prime Unless its 0 or 1."""

def isprime(x): 
    x  = abs(int(x)) 
    
    if x < 2: 
        return "less 2", False 
    elif x == 2: 
        return True 
    elif x % 2 == 0 : 
        return False  
    else: 
        for n in range(3, int(x**0.5)+2,2): 
            if x % n == 0: 
                return n, False  
        return True 
    
print("Please, input your number:") 
number = input() 

if isprime(number): 
    print(number,"is a Prime number.") 
else: 
    print(number,"is a Composite number.")  