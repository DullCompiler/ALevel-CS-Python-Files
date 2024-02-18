class Shape2: 
    def __init__(self):
        self.__colour="blue"
        self.name="square" 
    
    def getColour(self):
        print("Colour is: ", self.__colour) 
    
    def getName(self):
        print("name is: ", self.name) 

    def setColour(self, col):
        self.__colour=col

#instantiating an object called s 
s=Shape2() 
#printing the name by calling the getName method
print(s.getName()) 

#changing the shape's name to triangle and using the getName and getColour methods to print out the name and colour
s.name="triangle"
print(s.getName()) 
print(s.getColour())

#trying to change the colour attribute to red... what happens?
s.setColour("Red")
print(s.getColour())