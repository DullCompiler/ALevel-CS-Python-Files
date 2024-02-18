#Variables
passwords=[["Raspi"], ["pi"], ["password"]]
usermenu=True
account=0
username=1
password=2

#Menu
while usermenu==True:
    userchoice=input("Add Accounts: 1 | Find Account Details: 2 | Exit: 3 : ")
    userloop=True
#Append Account
    if userchoice=="1":
        while userloop==True:
            passwords[account].append(input("Please enter an account name: "))
            passwords[username].append(input("Please enter a username: "))
            passwords[password].append(input("Please enter a password: "))
            if input("Continue: y | Exit: n ").lower()=="n":
                userloop=False
#Find Account
    elif userchoice=="2":
        while userloop==True:
            index=passwords[0].index(input("Please enter the account name: "))
            print("User details:", passwords[[account][index]], passwords[[username][index]], passwords[[password][index]])
            if input("Continue: y | Exit: n ").lower()=="n":
                userloop=False
            
#Exit
    elif userchoice=="3":
        userloop=False
        usermenu=False
#Incorrect input
    else:
        print("Invalid input: err01")