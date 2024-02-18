# animal superclass

class Animal():
        
    def setWeight(self, w):
        self.w=w

    def setLength(self, l):
        self.l=l
        
    def getLength(self):
        return (self.l)

    def getWeight(self):
        return (self.w)

# subclass Bird inherits Animal class
class Bird(Animal):
     
    def setWingSpan(self, ws):
        self.ws=ws
       
    def setAltitude(self, a):
        self.a=a
             
    def getWingSpan(self):
        return(self.ws)
       
    def getAltitude(self):
        return(self.a)

# subclass Fish inherits Animal class
class Fish(Animal):

    def setNumberOfFins(self, fins):
        self.fins=fins
        
    def setDepth(self, depth):
        self.depth=depth
        
    def getNumberOfFins(self):
        return(self.fins)
        
    def getDepth(self):
        return(self.depth)

# subclass Mammal inherits Animal class
class Mammal(Animal):
    
    def setNumberofLegs(self, legs):
        self.legs=legs
		
    def setGestationPeriod(self, gperiod):
        self.gperiod=gperiod

#create the objects
eagle=Bird()
sparrow=Bird()
trout=Fish()
salmon=Fish()
elephant=Mammal()
human=Mammal()

# set attributes
trout.setWeight(2)
trout.setDepth(10)
trout.setLength(0.50)

eagle.setWeight(10)
eagle.setWingSpan(2)
eagle.setLength(0.50)

sparrow.setWeight(0.5)
sparrow.setLength(0.10)

#retrive attributes
print(eagle.getWeight())
print(eagle.getLength())
print(sparrow.getWeight())
print(sparrow.getLength())