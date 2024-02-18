print("What is the highest number you want to multiply to")
highestNumber = int(input())
print("What is the number you would like to multiply by")
multiplier = int(input())
number = 2
numberOut = 0

while number <= highestNumber:
		numberOut = multiplier * number
		print(numberOut)
		number = number + 1