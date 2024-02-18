import random

#2D List
animals = [["Salmon", "Pollock", "Cod"],
           ["Parrot", "Duck", "Wren"],
           ["Camel", "Lion", "Tiger"]]

#Printing Lines
print("Birds: ", animals[1])
print("Mammals: ", animals[2])

#Printing Specific Values
print(animals[1][2])
print(animals[0][1])
print(animals[2][0])

#Random Value Attainer
a=int((random.randint(0,2)))
b=int((random.randint(0,2)))
print("random value:", animals[a][b])