#importing
import random

#initialise TTS engine
import pyttsx3

#variables
turns=0
varied=0
simonstask=""
engine=pyttsx3.init()

#getting instructions
simon_says = ["Hands on head", "Hands on ears", "Right hand up", "Left hand up", "Hands on shoulders"]

#routine definition
while turns<10:
    #getting outputs
    index = int(random.randint(0,4))
    instruction = simon_says[index]
    varied=random.randint(0,1)
    
    #printing outputs + determining variabiltiy
    if varied!=1:
        say=("Simon says", (str(instruction)))
        engine.say((str(say)))
        print("Simon says", instruction.lower())
        engine.runAndWait()
    else:
        engine.say(str((instruction)))
        print(instruction)
        engine.runAndWait()
    
    #adding to turns
    turns=turns+1
print("Game Over")