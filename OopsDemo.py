class Calculator:
    num = 100
    def __init__(self, a, b):
        print("I am called automatically")
        self.a = a
        self.b = b

    def getData(self):
        print("I am executing class")

    def summation(self):
        return self.a + self.b + Calculator.num


#obj = Calculator()
#obj.getData()
#print(obj.num)

obj = Calculator(2, 3)
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)
obj.getData()
print(obj1.summation())