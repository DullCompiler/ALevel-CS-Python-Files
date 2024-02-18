import random
from re import L

#variables
words=["ham", "cucumber", "spice", "rishi", "hazmat", "valve"]
word = words[random.randint(0,5)]
wordlen=len(word)
firstlet=word[0]
lastlet=word[wordlen-1]
chances=5
end=False

#loop
while end!=True:
    while chances!=0:
        while chances!=1:
            print("The first letter is", firstlet)
            guess=input("Guess the word: ")
            if guess == word:
                print("correct")
                end=True
                chances=chances-1
            else:
                chances=chances-1
                guess=input("Guess the word: ")
                if guess == word:
                    print("correct")
                    end=True
                    chances=chances-1
                else:
                    chances=chances-1
                    print("The last letter is", lastlet)
                    guess=input("Guess the word: ")
                    if guess == word:
                        print("correct")
                        end=True
                        chances=chances-1
                    else:
                        chances=chances-1
                        guess=input("Guess the word: ")
                        if guess == word:
                            print("correct")
                            end=True
                            chances=chances-1
                        else:
                            chances=chances-1
                            guess=input("Guess the word: ")
                            if guess == word:
                                print("correct")
                                end=True
                                chances=chances-1
                            else:
                                print("The word was", word)