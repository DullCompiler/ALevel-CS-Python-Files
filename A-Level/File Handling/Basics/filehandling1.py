#print out line by line
file = open("/Users/aleden/Library/CloudStorage/OneDrive-Personal/Documents/Programming/Python/A-Level/File Handling/Basics/quick.txt","r")

for line in file:
    print(line.strip())