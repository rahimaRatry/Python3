#take a value from the user and check if that is less or greater than 10.

print('Please, Enter a value: ')
a = int(input())
if a<10:
    if ( a % 2 ):
        print('less, yes')
    else:
        print('less, no')
else:
    if( a % 3 ) == 0:
        print('greater, yes')
    else:
        print('greater, yes')