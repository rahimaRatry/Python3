"""__init__(self,[...])-this method constructs the class and __del__(self)-this method destructs the class."""
#example- 

class MyClass:
    """ A custom class for nothing."""

    def __init__(self, var):
        self.var = var 

    def __del__(self): 
        del self.var 
