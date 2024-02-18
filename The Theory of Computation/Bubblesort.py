import random

#creates datset
dataset=[]

while len(dataset) < 100:
    new_input = random.randint(1, 100)
    if new_input not in dataset:
        dataset.append(new_input)
print("Before sort: ", dataset)
print("")

#defines bubble sort algorithm subroutine
def bubbleSort(datatset):
    length = len(dataset)
    swapped = False
    for i in range(length-1):
        for j in range(0, length-i-1):
            if dataset[j] > datatset[j + 1]:
                swapped = True
                dataset[j], datatset[j + 1] = dataset[j + 1], dataset[j]    
        if not swapped:
            return

#starts bubble sort algorithm
bubbleSort(dataset)
print("After sort ", dataset)