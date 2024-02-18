#Q3
number=0
c=1
while (number<1) or (number>10):
    number=int(input("Enter a positive whole number: "))
    if int(number) > 10:
        print("Number is too large")
    else:
        if int(number) < 1:
            print("Not a positive number")

for k in range(0, (number - 1)):
    print(c)
    c=(c*(number-1-k)//(k+1))
 
#Q5
input1=input("Enter the first word: ")
input2=input("Enter the second word: ")
samesame=True
for letter in range(1, len(input1)):
   if input1.count(input1[letter]) > input2.count(input1[letter]):
       samesame=False
if samesame==True:
    print("Yes, they can be made from each other")
else:
    print("No, they cannot be made from each other")