def num_dogs():
    total_dogs=int(input("How many dogs have you walked? : "))
    return total_dogs

def num_days():
    total_days=int(input("How many days have you walked? : "))
    return total_days

def num_walks(total_dogs, total_days):
    total_walks=total_dogs*total_days
    return total_walks

def total_charge(total_walks):
    total_cost=total_walks*4
    return total_cost

def invoice(total_dogs, total_days, total_walks, total_cost):
    print("Invoice: Total Dogs Walked:",total_dogs, " Total Days Walked:", total_days, "Total Walks:", total_walks, "Total Cost:", total_cost)

total_dogs = num_dogs()
total_days = num_days()
total_walks = num_walks(total_dogs,total_days)
total_cost = total_charge(total_walks)
invoice(total_dogs, total_days, total_walks, total_cost)