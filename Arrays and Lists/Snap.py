import random
import time

rand=0
loop=True
turns=0
suits = ["♥", "♦", "♣", "♠"]
deck = []
cardnum=""

#Sets Up Deck
for suit in suits:
    for card in range(13):
        if (card+1) == 1:
            deck.append(str("A")+(suit))
        elif (card+1) == 11:
            deck.append(str("J")+(suit))
        elif (card+1) == 12:
            deck.append(str("Q")+(suit))
        elif (card+1) == 13:
            deck.append(str("K")+(suit))
        else:
            deck.append(str((card+1))+(suit))

random.shuffle(deck)
player1=deck[0:26]
player2=deck[26:56]

#Running Game
p1c=player1[0]
p2c=player2[0]
pile=[]
while loop==True:
    if not player1 or not player2 or turns>120:
        loop=False
    else:
        if loop==True:
            p1c=player1[0]
            p2c=player2[0]
            player1.pop(0)
            player2.pop(0)
            pile.append(p1c)
            pile.append(p2c)
            print("")
            print("Player 1 picked", p1c)
            print("Player 2 picked", p2c)
            if p1c[0] == p2c[0]:
                print("Snap")
                rand=random.randint(0,1)
                if rand == 0:
                    player1=player1+pile
                    print("Player 1 Claims Snap and Wins Pile")
                else:
                    player2=player2+pile
                    print("Player 2 Claims Snap and Wins Pile")
            time.sleep(0)
            turns=turns+1

#End Arguments
if turns>120:
    print("You gave up after playing 120 turns")
elif not player1 and not player2:
    print("No Snaps Occured, it is a draw!")
elif len(player1)==0:
    print("Player 2 Wins")
    print(len(player1))
elif len(player2)==0:
    print("Player 1 Wins")