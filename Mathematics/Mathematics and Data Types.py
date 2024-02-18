#Shopping List
loopend=False
slist=[]
addto=""

#Listing Shopping List
def listinglist(slist):
    print(slist)

#Adding to Shopping List
def addlist(slist):
    addto=input("Please enter what you want to add:")
    slist.append(addto)

while loopend == False:
    print("Shopping List menu")
    print("1 to List Shopping List")
    print("2 to Add to Shopping list")
    print("e to exit")
    inp=input("Input:")
    if str(inp)=="1":
        listinglist(slist)
    elif str(inp)=="2":
        addlist(slist)
    elif str(inp)=="e":
        loopend=True
    else:
        print("Please enter a valid input")