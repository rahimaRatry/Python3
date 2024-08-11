
""" If we pass any iterable object in 'iter()' function (which is built in function),then that returns 
an iterator. By using '__next__()' method we can access the next element of the iterator. After accessing 
all the elements, when there is no element to access then Python throws the 'StopIteration' Error."""

# this iterator works like built-in 'range()' function, but reversly.

class revrange: 

    def __init__(self,n): 
        self.n = n 
        self.i = n 

    def __iter__(self): 
        return self 
    
    def __next__(self): 
        if self.n >= 0: 
            if self.i == self.n: 
                self.n = self.n - 1 
                return self.i 
            else: 
                self.i = self.n 
                self.n = self.n - 1 
                return self.i 
        else: 
            raise StopIteration 
        
for temp in revrange(5): 
    print(temp) 
