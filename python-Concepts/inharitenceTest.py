from const import constDemo

class parentChild(constDemo):
    a  = 0
    b =  0

    def __init__(self):
        self.a = constDemo.firstVariable
        self.b = constDemo.secondVariable

    def sumNum(self):
        print("in child class")
        print(self.a + self.b)
        return "in child class"
    
    
    def addNumbers(self):
        print("++++++++++++++++")

    
obj = parentChild()
obj.addNumbers()
print(obj.sumNum())