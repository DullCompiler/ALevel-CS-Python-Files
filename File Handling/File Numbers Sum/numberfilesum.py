#number sum
number = open("/Users/aleden/Library/CloudStorage/OneDrive-Personal/Documents/Programming/Python/A-Level/File Handling/File Numbers Sum/numbers.txt","r")
sum = 0

for line in number:
    sum=sum+int(line)
    
print("The sum for the file is", sum)