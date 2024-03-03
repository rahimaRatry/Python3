#if there is no error in try block then the exception block will not execute.

try: 
    a = 6 
    b = 7 
    print(a + b) 
except ValueError as e: 
    print(e) 
else: 
    print("There is no exception!") 
