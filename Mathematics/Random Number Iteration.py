import random

number = random.randint(1, 10)
guesscount = 1

while guesscount < 4:
    print("Guess a number between 1 and 10")
    guess = int(input())
    if guess==number:
        print("Correct, that took you ", guesscount, " guesses")
    else:
        print("Incorrect")
        guesscount=guesscount+1
print("The number was ", number)