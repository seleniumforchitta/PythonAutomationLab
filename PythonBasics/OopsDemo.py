# methods
# class variable 
# instance variable 
# constructor 

class Calculator:
    num = 100
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I am constructor - I am called automatically when object is created")
    
    def getData(self):
        print("I am getData method inside Calculator class")
    
    def summations(self):
        return self.a + self.b + Calculator.num # self.num can be used also for class variable
        

# instance variable - Attached to the object
# class variable - Attached to the class, not attached to the object 
    
cal = Calculator(3, 4)
cal.getData()
print(cal.num)
print(cal.summations())

cal = Calculator(13, 14)
print(cal.summations())






        