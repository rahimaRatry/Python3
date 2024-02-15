# take a number from the user and find that's factorial using recursive function.

def factorial(number):  #here factorial() is the recursive function and (number)is parameter or argument.
    if number == 0:
        return 1  #we know factroial of 0 is 1.
    else:
        return number *factorial(number-1)
print("Please, input your number:")
number = int(input())
print("Factorial of the number is:",factorial(number)) 