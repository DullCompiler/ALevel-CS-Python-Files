times_table = int(input("What Times Table do you want: "))
upperlimit = int(input("How High up the Table do you want to go? (1, ?): "))
answer = 0
print(f"Here is the {times_table} times table")
for x in range(1,upperlimit):
    answer = x * times_table
    print(f"{x} times {times_table} is {answer}")