#Introduction
print("Welcome to the Guess the Word Game")
print("Player 1 please enter the word")
secretword=input("Secret word:")
print("Player 2 you must guess the secret word")
print("The word has", len(secretword), "letters")

#Game
for x in range(3):
    usrinp=input("Player 2 enter a letter: ")
    if usrinp in secretword:
        count=0
        for x in secretword:
            if x == usrinp:
                count=count+1
        print("letter:", usrinp, "count:", count)

guess=input("Guess the secret word")
if guess==secretword:
        print("Correct answer")
else:
    print("Secret word was", secretword)