#take an input from the user and check if that equal, less or greater than 5.

print('Please, Enter a value: ')
a = int(input())
if a== 5:
    print('a is equal to 5.')
elif a < 5 :
    print('a is less than 5.')
elif a > 5 and a < 10:
    print('a is inbetween 5 and 10.')
else:
    print('a is greater than 10.')