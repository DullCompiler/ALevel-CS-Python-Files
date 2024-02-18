#Print as list (without /n)
file = open("/Users/aleden/Library/CloudStorage/OneDrive-Personal/Documents/Programming/Python/A-Level/File Handling/Basics/quick.txt","r")

quicklist = []

for line in file:
    quicklist.append(line.strip())

print(quicklist)