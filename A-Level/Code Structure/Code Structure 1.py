#before
#def and_function(a, b):
#    if a == True and b == True:
#        return True
#    else:
#        return False   
#
#one = 4 == 4
#two = 2 == 2
#
#print(and_function(one, two))

#after
def and_function(a,b):
    if a == True and b == True:
        result = True
    else:
        result = True
    return result
    
one = 4==4
two = 2==2

print(and_function(one, two))