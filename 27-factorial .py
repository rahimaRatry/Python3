# write a python code to find the factorial of a number given by user.

print("Please, input your number:")
number = int(input())
temp = number
while number > 1:
    number -= 1
    temp = temp*number # Recursion.
if temp == 0:
    print("The factorial is: 1")  #because we know factorial of 0 is 1.
else:
    print("The factorial is:",temp) 