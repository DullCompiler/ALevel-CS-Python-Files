# Composition is another and often
# preferable way to associating classes with one another.

# building-room

class Building:

    def setHeight(self, height):
        self.height=height
        
    def setFootprint(self, footprint):
        self.footprint=footprint

    def getHeight(self):
        return (self.height)

    def getFootprint(self):
        return (self.height)

class Room:

    def __init__(self):
        self.building=Building()  # Composition  
     
    def setRoomArea(self, roomWidth, roomLength):
        self.roomArea = roomWidth*roomLength
                 
    def getRoomArea(self):
        return(self.roomArea)
       
kitchen=Room()
kitchen.setRoomArea(300, 200)
kitchen.building.setHeight(230)
kitchen.building.setFootprint(60000)
print(kitchen.building.getFootprint())
print(kitchen.building.getHeight())