
class CustomError(Exception): 
    #Example 
    def __init__(self,message): 
        self.message = message 
try: 
    raise CustomError("It is an Custom Error.") 
except CustomError as e: 
    print(e) 
