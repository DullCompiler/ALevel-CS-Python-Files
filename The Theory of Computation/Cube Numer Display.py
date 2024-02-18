#Devise a pseudocode algorithm which generates and prints all 3-digit numbers that equal the sum of the cubes of their individual digits.
#e.g. 153 satisfies this condition because 153 = 13  + 53 + 33 (In pseudocode, express this as 1**3 + 5**3 + 3**3)

uservalidation=False
userinput=0

while uservalidation==False:
    userinput=input("Please enter a number: ")
    if len(userinput) == 3:
        uservalidation=True
    else:
        print("Error 1: Input must three digits long")
num=int(userinput)

hundreds=num[0]
tens=num[e]