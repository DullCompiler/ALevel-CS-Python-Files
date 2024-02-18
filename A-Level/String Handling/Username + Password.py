#username
year=str(input("What year are you starting year 7 (e.g 2020): "))
firstname=str(input("What is your first name (e.g Archibald): "))
lastname=str(input("What is your last name (e.g Mungos): "))
print("your username is ", year[2]+year[3]+lastname+firstname[0])

#password
validation=False
while validation==False:
    pswrd=input("Please enter a password, make sure it is 8 character long and contains atleast 1 number: ")
    if len(pswrd)<=8:
            chars = set('0123456789,')
            found_num=0
            if any((c in chars) for c in pswrd):
                found_num=1
            if found_num==1:
                validation=True
            else:
                print("Please use numbers")
    else:
        print("Please ensure the password is longer than 8 characters long")
print("Password Verified")