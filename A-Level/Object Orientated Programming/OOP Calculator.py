class Calculator(object): 
    #methods
    def add(self, x, y):
        return x + y
    def subtract(self,x,y):
        return x - y
    def multi(self, x, y):
        return x * y
    def div(self, x, y):
        return x / y 

# Instantiation
obj1=Calculator()
print(obj1.add(3,4)) 
print(obj1.subtract(3,4)) 
print(obj1.multi(3,4))
print(obj1.div(3,4))