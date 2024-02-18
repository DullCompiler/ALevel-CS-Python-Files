#Variables
loop=False
secretword=""
usrinp=""
count=0

#Introduction
print("Welcome to the Guess the Word Game")
print("Player 1 please enter the word")
secretword=input("Secret word: ")
print("Player 2 you must guess the secret word")
print("The word has", len(secretword), "letters")

#Game
while loop==False:
    usrinp=input("Player 2 enter a letter: ")
    if usrinp in secretword:
        count=0
        for x in secretword:
            if x == usrinp:
                count=count+1
        print("letter:", usrinp, "count:", count)
    else:
        print("letter", usrinp, "is not in the secret word")
        answer=input("Do you want to guess the word? y/n :")
        if answer=="y":
            guess=input("Guess the secret word: ")
            if guess==secretword:
                print("Correct answer")
                loop=True
            else:
                print("Incorrect")