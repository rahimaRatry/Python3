
class SuperCalculator: 
    ''' Do addition, subtraction, multiplication, division, square and cube.''' 
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
    def square(self,a): 
        return a*a 
    def cube(self,a): 
        return a*a*a 

my_calculator = SuperCalculator() 

temp = my_calculator.addition(12,43) 
print("The sum is:",temp) 

temp = my_calculator.subtraction(45,43) 
print("The difference is:",temp) 

temp = my_calculator.multiplication(78,32) 
print("The product is:",temp) 

temp = my_calculator.division(56,7) 
print("The quotient is:",temp) 

temp = my_calculator.division(34,0) 
print("The quotient is:",temp) 

temp = my_calculator.square(5) 
print("The square is:",temp) 

temp = my_calculator.cube(3) 
print("The cube is:",temp)  
