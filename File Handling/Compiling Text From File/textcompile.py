#text compile
transcript1 = open("/Users/aleden/Library/CloudStorage/OneDrive-Personal/Documents/Programming/Python/A-Level/File Handling/Compiling Text From File/transcript1.txt","r")
transcript2 = open("/Users/aleden/Library/CloudStorage/OneDrive-Personal/Documents/Programming/Python/A-Level/File Handling/Compiling Text From File/transcript2.txt","r")
commes=[]
tran1mes=[]
tran2mes=[]
count=0

for line in transcript1:
    tran1mes.append(str(line.strip()))

for line in transcript2:
    tran2mes.append(str(line.strip()))

length=len(tran1mes)

while count<length:
    commes.append(tran1mes[count])
    commes.append(tran2mes[count])
    count=count+1
    
print(commes)