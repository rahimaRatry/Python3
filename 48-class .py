
class Calculator: 
    ''' Do addition, subtraction, multiplication and division.'''

# If we want to pass any value in class then we have to write '__init__' as the first method of the class.
# And it is called class constructor.
    
    def __init__(self, a, b):  
        self.a = a 
        self.b = b 
    def addition(self): 
        return self.a + self.b 
    def subtraction(self): 
        return self.a - self.b 
    def multiplication(self): 
        return self.a * self.b 
    def division(self): 
        try: 
            return  self.a / self.b 
        except ZeroDivisionError: 
            return "It is impossible to divide by zero." 
        
my_calculator = Calculator(45, 3) #'Calculator()= NameError-undefined variable'.which has occured for Indentation.

# To avoid this problem we should write the 'Calculator()' function under the class sequence.not in def. 

temp = my_calculator.addition() 
print(temp) 

temp = my_calculator.subtraction() 
print(temp) 

temp = my_calculator.multiplication() 
print(temp) 

temp = my_calculator.division() 
print(temp)   
