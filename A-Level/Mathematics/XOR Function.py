def xor_function(a, b):
    print("Xor Gate")
    if (a == True or b == True) and (a and b != True):
        c = True
    else:
        c = False
    print(c)

def or_function(a, b):
    print("Or Gate")
    if (a == True or b == True):
        c = True
    else:
        c = False
    print(c)

def and_function(a, b):
    print("And Gate")
    if (a == True and b == True):
        c=True
    else:
        c = False
    print(c)

a=input("Input: True / False: ")
if a.lower=="true":
    a=True
elif a.lower=="false":
    a=False
else:
    print("Input Error")

b=input("Input: true / false: ")
if b=="true":
    b=True
elif b=="false":
    b=False
else:
    print("Input Error")

or_function(a, b)
xor_function(a, b)
and_function(a, b)