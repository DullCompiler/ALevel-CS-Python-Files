#Imports
from os import system
import time

#Variable Setup
Bal=3544
Choice=""
cont=False

#Subroutines

#Show Balance
def ShowBal(Bal):
    print("Balance:", Bal)

#Deposit
def Deposit(Bal):
    Bal=Bal+int(input("Enter amount to deposit: "))
    return Bal

#Withdraw
def Withdraw(Bal):
    Bal=Bal-int(input("Enter amount to withdraw: "))
    return Bal

#Main Menu
def Menu(Choice, Bal, cont):
    while cont==True:
        print("For deposit press d")
        print("For withdrawal press w")
        print("To check your balance, press b")
        print("To exit press e")
        Choice=input("Enter choice here: ")
        if Choice=="d":
            Bal=Deposit(Bal)
            time.sleep(2)
            clear()
        elif Choice=="w":
            Bal=Withdraw(Bal)
            clear()
        elif Choice=="b":
            ShowBal(Bal)
            clear()
        elif Choice=="e":
            exit()
        else:
            print("Error 01: please enter correct choice")

#Clear Shell
def clear():
    time.sleep(1)
    _ = system('clear')

#Main Program

print("Welcome to the Bank of America ATM")

#Pin Code
while cont==False:
    if input("Enter Pin: ")=="7387":
        clear()
        cont=True
    else:
        print("Incorrect Pin")

Menu(Choice, Bal, cont)