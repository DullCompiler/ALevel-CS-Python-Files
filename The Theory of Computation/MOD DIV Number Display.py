#e.g. x = 27 MOD 4  will put the value 3 in x. 
#		DIV returns the integer result of the division.
#		e.g. y = 27 DIV 4 will put the value 6 in y.
#		Write pseudocode statements to allow the user to input a 3-digit number, and then output the individual digits in the number. Using MOD and DIV.
#		e.g. If the user enters 465, the output should be “The digits are 4    6    5”

uservalidation=False
userinput=0

while uservalidation==False:
    userinput=input("Please enter a number: ")
    if len(userinput) == 3:
        uservalidation=True
    else:
        print("Error 1: Input must three digits long")
num=int(userinput)

hundreds=num//100
temp=num%100
tens=temp//10
units=num%10
sumcubed=((hundreds**3)+(tens**3)+(units**3))

print(hundreds, tens, units)
if sumcubed==num:
    print(sumcubed, "is the total of", num, "cubed")