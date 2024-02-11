# take a numeber from user and print that's multiplication table.

print("Please, input the number:")
number = int(input())
count = 1
while count<=10:
    print(number,'X',count,'=',number*count)
    count += 1
    