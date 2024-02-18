import random

#gather words
word1=input("Input Word One: ")
word2=input("Input Word Two: ")
word3=input("Input Word Three: ")

#concatenate words
password_pre=(word1+word2+word3).lower()
password_post=""

#replace vowels
for letter in password_pre:
    if letter == "a":
        password_post = password_post + chr(random.randint(33, 37))
    elif letter == "e":
        password_post = password_post + chr(random.randint(38, 42))
    elif letter == "i":
        password_post = password_post + chr(random.randint(43, 47))
    elif letter == "o":
        password_post = password_post + chr(random.randint(58, 61))
    elif letter == "u":
        password_post = password_post + chr(random.randint(91, 94))
    else:
        password_post = password_post + letter
        
#print results
print("Before yassification: ", password_pre)
print("After yassification", password_post)