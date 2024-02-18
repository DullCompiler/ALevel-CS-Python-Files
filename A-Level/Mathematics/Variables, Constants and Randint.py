import random

inpcorrect=False
usrlow=0
usrhigh=0
number=0

while inpcorrect==False:
    usrlow=input("Insert lower randint number: ")
    usrhigh=input("Insert higher randing number: ")
    if usrlow.isdigit() and usrhigh.isdigit():
        if int(usrlow)>int(usrhigh):
            print("Error 2: Lower number acannot be higher than the higher number, try again")
        else:
            inpcorrect=True
    else:
        print("Error 1: Inputs are not intergers")
number = random.randint(int(usrlow), int(usrhigh))

print(number)