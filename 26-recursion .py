"""Recursive functions are functions that calls itself.
It is always made up of 2 portions, the base case and the recursive case. 
The base case is the condition to stop the recursion. The recursive case is the part where the function calls on itself."""

def counter(num):
    print(num)
    num += 1
    counter(num)

counter(1) 
