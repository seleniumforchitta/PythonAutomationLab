from OopsDemo import Calculator

class Childcal(Calculator):
    num2 = 200
    
    def __init__(self): ## you have to create this constructor if parent has a parameterized constructor
        Calculator.__init__(self, 3, 4)
        
    def getCompleteData(self):
        return self.num2 + self.num #+ self.summations()

childobj = Childcal()
print(childobj.getCompleteData())

