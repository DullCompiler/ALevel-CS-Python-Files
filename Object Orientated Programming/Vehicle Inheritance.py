# vehicle superclass

class Vehicle():
        
    def setWeight(self, w):
        self.w=w

    def setMaxOccupancy(self, mo):
        self.mo=mo
        
    def setPower(self, p):
        self.p=p
        
    def getWeight(self):
        return (self.w)
    
    def getMaxOccupancy(self):
        return (self.mo)
    
    def getPower(self):
        return (self.p)

# subclass Bird inherits Animal class
class Car(Vehicle):
     
    def setWheelNumber(self, wn):
        self.wn=wn
       
    def setHorsePower(self, hp):
        self.hp=hp
        
    def setTransmission(self, t):
        self.t=t
             
    def getWheelNumber(self):
        return (self.wn)
    
    def getHorsePower(self):
        return (self.hp)

    def getTransmission(self):
        return (self.t)
        
# subclass Fish inherits Animal class
class Plane(Vehicle):

    def setTypePlane(self, tp):
        self.tp=tp
    
    def setWingspan(self, ws):
        self.ws=ws

    def setMaxAltitude(self, ma):
        self.ma=ma

    def getTypePlane(self):
        return(self.tp)

    def getWingSpan(self):
        return(self.ws)
       
    def getMaxAltitude(self):
        return(self.ma)

		
#create the objects
minivan=Car()
eighteenwheeler=Car()
seaplane=Plane()
passangerjet=Plane()

# set attributes
minivan.setWheelNumber(4)
minivan.setHorsePower(290)
minivan.setTransmission("Manual")

eighteenwheeler.setWheelNumber(18)
eighteenwheeler.setHorsePower(600)
eighteenwheeler.setTransmission("Manual")

seaplane.setTypePlane("Passenger")
seaplane.setWingspan(36)
seaplane.setMaxAltitude(13000)

passangerjet.setTypePlane("Passenger")
passangerjet.setWingspan(262)
passangerjet.setMaxAltitude(43000)

#retrive attributes
print(minivan.getWeight())
print(minivan.getMaxOccupancy())
print(seaplane.getWeight())
print(seaplane.getMaxOccupancy())