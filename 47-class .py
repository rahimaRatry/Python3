# A class is a group of objects which has some common properties and functions(called methods).

class Calculator: 
    """ Do addition, subtraction, multiplication and division.""" 

    def addition(self, a, b):  # here 'self' is a conventional name.it is a reference of instance variable.
        return a + b 
    def subtraction(self, a, b): 
        return a - b 
    def multiplication(self, a, b): 
        return a * b 
    def division(self, a, b): 
        try: 
            return a / b 
        except ZeroDivisionError: 
            return "It is impossible to divide by zero." 
        
my_calculator = Calculator() 

temp = my_calculator.addition(12,78) 
print(temp) 

temp = my_calculator.subtraction(12,4) 
print(temp) 

temp = my_calculator.multiplication(9, 57) 
print(temp) 

temp = my_calculator.division(45, 9) 
print(temp) 

temp = my_calculator.division(23, 0) 
print(temp) 
