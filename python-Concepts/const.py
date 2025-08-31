class constDemo:
    firstVariable  = 10
    secondVariable = 20

    def __init__(self, a , b):
        self.constValue1 = a
        self.constValue2 = b
        print("---------------------------------")
    
    
    def addNumbers(self):
        print("[INFO] adding numbers....")
        print(self.constValue1 + self.constValue2)
        print("addition sucessfully done")


# con = constDemo(2, 3)
# con.addNumbers()