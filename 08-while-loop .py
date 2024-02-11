# print the sum of 1 to 100./ 1+2+3+...+100 = ?

n = 1
temp = 0                # without loop: 
while n <= 100:          #n=100 
    temp = temp + n      #temp = n*(n+1)
    n = n + 1            #temp = temp/2
print(temp)              #print(temp) 