#take a number from the user and check if that is positive or negative.

print('Please, Enter a number:')
number = float(input())
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")