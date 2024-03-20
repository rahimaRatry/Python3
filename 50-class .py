# Inheritance...

class Calculator:  
    """ Do addition, subtraction, multiplication and division.""" 
    def addition(self,a,b): 
        return a+b 
    def subtraction(self,a,b): 
        return a-b 
    def multiplication(self,a,b): 
        return a*b 
    def division(self,a,b): 
        try: 
            return a/b 
        except ZeroDivisionError: 
            return "It is impossible to divide by zero." 
        
class SuperCalculator(Calculator): #Inherited. Child class of Calculator. Do square and cube.

    def square(self,a): 
        return a*a  
    def cube(self,a): 
        return a*a*a 

my_calculator = SuperCalculator() 

temp = my_calculator.addition(56,75) 
print(temp)  

temp = my_calculator.subtraction(45,23) 
print(temp)  

temp = my_calculator.multiplication(23,3) 
print(temp)  

temp = my_calculator.division(23,4) 
print(temp)  

temp = my_calculator.square(4) 
print(temp)  

temp = my_calculator.cube(6) 
print(temp) 
