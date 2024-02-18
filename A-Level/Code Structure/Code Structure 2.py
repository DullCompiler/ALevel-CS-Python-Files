##before
##def password_check():
##    password = "12345"
##    entered_pass = ""
##    pass_not_valid = password != entered_pass
##    attempts = 0
##   while pass_not_valid and attempts < 3:
##        print("Enter a password:")
##        entered_pass = input()
##        attempts = attempts + 1
##        if password == entered_pass:
##            break
##    if password != entered_pass:
##        return "Access Denied"
##    else:
##        return "Access Granted"
##
##print(password_check())

##after
def password_check():
    password = "12345"
    entered_pass = ""
    pass_not_valid = password != entered_pass
    attempts = 0
    access = ""
    while pass_not_valid and attempts < 3:
        entered_pass = input("Enter a password:")
        if password == str(entered_pass):
            pass_not_valid=3
            attempts=3
        attempts = attempts + 1
    if password != entered_pass:
        access="Access Denied"
    else:
        access="Access Granted"
    return access

print(password_check())