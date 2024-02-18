crust=""
typep=""
size=0
cost=0
cheese=True

crust=input("Do you want thin or thick crust pizaa").lower()
size=input("What sized pizza do you want? 8, 10, 12, 14, 18").lower()
cheese=input("Do you want cheese on your pizza? True or False").lower()
typep=input("Do you want a Margherita, Vegetable, Vegan, Hawaiian or Meat Feast").lower()

def crust(crust, cost):
    if crust == "thin" or "thick":
        if crust == "thin":
            cost=cost+8
        elif crust == "thick":
            cost=cost+10
        else:
            print("error wrong input")

def size(size, cost):
    if size == '8' or '10' or '12' or '14' or '18':
        if size == '12' or '14' or '14':
            cost=cost+2
    else:
        print("error wrong input")

def cheese(cheese, cost):
    if cheese != True:
        cost=cost-0.5

def typep(typep, cost):
    if typep == "margherita" or "vegetable" or "vegan" or "hawaiian" or "meat feast":
        if typep == "vegetable" or "vegan":
            cost=cost+1
        elif typep == "hawaiian" or "meat feast":
            cost=cost+2
    else:
        print("error wrong input")