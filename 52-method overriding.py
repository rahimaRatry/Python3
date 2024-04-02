
class Calculator:  
    """ Do addition, subtraction, multiplication and division."""

    def addition(self, a,b): 
        return a+b 
    def subtraction(self,a,b): 
        return a-b 
    def multiplication(self,a,b): 
        return a*b 
    def division(self,a,b): 
        try: 
            return a/b 
        except ZeroDivisionError: 
            return "It is impossioble to divide by zero." 
        
class SuperCalculator(Calculator): 
    """ Do addition,subtraction,multiplication,division,square and cube."""
    def addition(self, a, b, c): 
        return a+b+c    # Method Overriding of addition method. 
    def square(self,a): 
        return a*a 
    def cube(self,a): 
        return a*a*a 
    
my_calculator = SuperCalculator() 

temp = my_calculator.addition(23,56,34) 
print(temp) 

temp = my_calculator.subtraction(45,23) 
print(temp) 

temp = my_calculator.multiplication(51,32) 
print(temp) 

temp = my_calculator.division(834,24) 
print(temp) 

temp = my_calculator.square(12) 
print(temp) 

temp = my_calculator.cube(4) 
print(temp) 
