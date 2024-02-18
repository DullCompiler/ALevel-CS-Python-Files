#carpet calculator
import sys

len1=int(input("Enter Length One: "))
len2=int(input("Enter Length Two: "))
width=4
length=0
    
#longest side
if len1>len2:
    if len1>4:
        length=len1
    elif len1<=4:
        width=len1
        length=len2

if len2>len1: 
    if len2>4:
        length=len2
    elif len2<=4:
        width=len2
        length=len1

if len1>4 and len2>4:
    print("error: dimensions incapable of printing")
    sys.exit()

if width<4:
    width=4

print("width: ", width)
print("length: ", length)
cost=(width*length)*10
print("cost:", cost)