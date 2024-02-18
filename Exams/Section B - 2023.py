#import modules
import time

#variables
usr_input = ""
validation = False

#get user input and validate

#define Subroutine
def get_input(usr_input, validation):
    #get input
    usr_input = str(input("Please enter a string that is five to seven chareacters long, uppercase, contraining no repeating values and has an ASCII sum between 420 and 600: "))
    
    #print(input) #debugging
    #print(usr_input) #debugging
    #print(len(usr_input)) #debugging
    
    #check input length
    time.sleep(1)
    if int(len(usr_input)) >= 5 and int(len(usr_input)) <= 7:
        print("length is valid")
        validation = validation + 1
    else:
        print("length is invalid")
        get_input(usr_input, validation)
        
    #check input is uppercase
    time.sleep(1)
    if usr_input.isupper() == True:
        print("input is uppercase")
        validation = validation + 1
    else:
        print("input is not uppercase")
        get_input(usr_input, validation)
    
    #check ascii sum
    time.sleep(1)
    ascii_sum = 0
    for i in usr_input:
        ascii_sum = ascii_sum + ord(i)
    if ascii_sum >= 420 and ascii_sum <= 600:
        print("ascii sum is valid")
        validation = validation + 1
    else:
        print("ascii sum is invalid")
        get_input(usr_input, validation)
    
    #check for repeating values
    time.sleep(1)
    if len(usr_input) == len(set(usr_input)):
        print("no repeating values")
        validation = validation + 1
    else:
        print("repeating values")
        get_input(usr_input, validation)
    
    #check validation
    time.sleep(1)
    if validation == 4:
        print("input is valid")
        return usr_input
    else:
        print("input is invalid")
        get_input(usr_input, validation)

#call subroutine
usr_input = get_input(usr_input, validation)