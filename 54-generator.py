""" Generator is another type of iterator. we use 'yield' statement here."""

def reverange(n): 
    while n >= 0: 
        yield n 
        n = n - 1 
        
for temp in reverange(5): 
    print(temp) 
