#import modules
import os
import random
import time

#gameboards
player1refrence=[[" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],]

player1gameboard=[[" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],]

player2refrence=[[" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],]

player2gameboard=[[" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],
                 [" ", " ", " ", " ", " ", " ", " ", " ",],]

#subroutines

#P1 Refrence Board
def displarefpb1(player1refrence):
    print("Player One's Board Layout")
    print(" ", player1refrence[0][0], "│", player1refrence[0][1], "│", player1refrence[0][2], "│", player1refrence[0][3], "│", player1refrence[0][4], "│", player1refrence[0][5], "│", player1refrence[0][6], "│", player1refrence[0][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1refrence[1][0], "│", player1refrence[1][1], "│", player1refrence[1][2], "│", player1refrence[1][3], "│", player1refrence[1][4], "│", player1refrence[1][5], "│", player1refrence[1][6], "│", player1refrence[1][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1refrence[2][0], "│", player1refrence[2][1], "│", player1refrence[2][2], "│", player1refrence[2][3], "│", player1refrence[2][4], "│", player1refrence[2][5], "│", player1refrence[2][6], "│", player1refrence[2][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1refrence[3][0], "│", player1refrence[3][1], "│", player1refrence[3][2], "│", player1refrence[3][3], "│", player1refrence[3][4], "│", player1refrence[3][5], "│", player1refrence[3][6], "│", player1refrence[3][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1refrence[4][0], "│", player1refrence[4][1], "│", player1refrence[4][2], "│", player1refrence[4][3], "│", player1refrence[4][4], "│", player1refrence[4][5], "│", player1refrence[4][6], "│", player1refrence[4][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1refrence[5][0], "│", player1refrence[5][1], "│", player1refrence[5][2], "│", player1refrence[5][3], "│", player1refrence[5][4], "│", player1refrence[5][5], "│", player1refrence[5][6], "│", player1refrence[5][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1refrence[6][0], "│", player1refrence[6][1], "│", player1refrence[6][2], "│", player1refrence[6][3], "│", player1refrence[6][4], "│", player1refrence[6][5], "│", player1refrence[6][6], "│", player1refrence[6][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1refrence[7][0], "│", player1refrence[7][1], "│", player1refrence[7][2], "│", player1refrence[7][3], "│", player1refrence[7][4], "│", player1refrence[7][5], "│", player1refrence[7][6], "│", player1refrence[7][7])
    print("")

#P2 Refrence Board
def displarefpb2(player2refrence):
    print("Player Two's Board Layout")
    print(" ", player2refrence[0][0], "│", player2refrence[0][1], "│", player2refrence[0][2], "│", player2refrence[0][3], "│", player2refrence[0][4], "│", player2refrence[0][5], "│", player2refrence[0][6], "│", player2refrence[0][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2refrence[1][0], "│", player2refrence[1][1], "│", player2refrence[1][2], "│", player2refrence[1][3], "│", player2refrence[1][4], "│", player2refrence[1][5], "│", player2refrence[1][6], "│", player2refrence[1][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2refrence[2][0], "│", player2refrence[2][1], "│", player2refrence[2][2], "│", player2refrence[2][3], "│", player2refrence[2][4], "│", player2refrence[2][5], "│", player2refrence[2][6], "│", player2refrence[2][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2refrence[3][0], "│", player2refrence[3][1], "│", player2refrence[3][2], "│", player2refrence[3][3], "│", player2refrence[3][4], "│", player2refrence[3][5], "│", player2refrence[3][6], "│", player2refrence[3][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2refrence[4][0], "│", player2refrence[4][1], "│", player2refrence[4][2], "│", player2refrence[4][3], "│", player2refrence[4][4], "│", player2refrence[4][5], "│", player2refrence[4][6], "│", player2refrence[4][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2refrence[5][0], "│", player2refrence[5][1], "│", player2refrence[5][2], "│", player2refrence[5][3], "│", player2refrence[5][4], "│", player2refrence[5][5], "│", player2refrence[5][6], "│", player2refrence[5][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2refrence[6][0], "│", player2refrence[6][1], "│", player2refrence[6][2], "│", player2refrence[6][3], "│", player2refrence[6][4], "│", player2refrence[6][5], "│", player2refrence[6][6], "│", player2refrence[6][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2refrence[7][0], "│", player2refrence[7][1], "│", player2refrence[7][2], "│", player2refrence[7][3], "│", player2refrence[7][4], "│", player2refrence[7][5], "│", player2refrence[7][6], "│", player2refrence[7][7])
    print("")

#P1 Gameboard
def displaregpb1(player2gameboard):
    print(" ", player2gameboard[0][0], "│", player2gameboard[0][1], "│", player2gameboard[0][2], "│", player2gameboard[0][3], "│", player2gameboard[0][4], "│", player2gameboard[0][5], "│", player2gameboard[0][6], "│", player2gameboard[0][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2gameboard[1][0], "│", player2gameboard[1][1], "│", player2gameboard[1][2], "│", player2gameboard[1][3], "│", player2gameboard[1][4], "│", player2gameboard[1][5], "│", player2gameboard[1][6], "│", player2gameboard[1][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2gameboard[2][0], "│", player2gameboard[2][1], "│", player2gameboard[2][2], "│", player2gameboard[2][3], "│", player2gameboard[2][4], "│", player2gameboard[2][5], "│", player2gameboard[2][6], "│", player2gameboard[2][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2gameboard[3][0], "│", player2gameboard[3][1], "│", player2gameboard[3][2], "│", player2gameboard[3][3], "│", player2gameboard[3][4], "│", player2gameboard[3][5], "│", player2gameboard[3][6], "│", player2gameboard[3][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2gameboard[4][0], "│", player2gameboard[4][1], "│", player2gameboard[4][2], "│", player2gameboard[4][3], "│", player2gameboard[4][4], "│", player2gameboard[4][5], "│", player2gameboard[4][6], "│", player2gameboard[4][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2gameboard[5][0], "│", player2gameboard[5][1], "│", player2gameboard[5][2], "│", player2gameboard[5][3], "│", player2gameboard[5][4], "│", player2gameboard[5][5], "│", player2gameboard[5][6], "│", player2gameboard[5][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2gameboard[6][0], "│", player2gameboard[6][1], "│", player2gameboard[6][2], "│", player2gameboard[6][3], "│", player2gameboard[6][4], "│", player2gameboard[6][5], "│", player2gameboard[6][6], "│", player2gameboard[6][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player2gameboard[7][0], "│", player2gameboard[7][1], "│", player2gameboard[7][2], "│", player2gameboard[7][3], "│", player2gameboard[7][4], "│", player2gameboard[7][5], "│", player2gameboard[7][6], "│", player2gameboard[7][7])
    print("")    

#P2 Gameboard
def displaregpb2(player1gameboard):
    print(" ", player1gameboard[0][0], "│", player1gameboard[0][1], "│", player1gameboard[0][2], "│", player1gameboard[0][3], "│", player1gameboard[0][4], "│", player1gameboard[0][5], "│", player1gameboard[0][6], "│", player1gameboard[0][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1gameboard[1][0], "│", player1gameboard[1][1], "│", player1gameboard[1][2], "│", player1gameboard[1][3], "│", player1gameboard[1][4], "│", player1gameboard[1][5], "│", player1gameboard[1][6], "│", player1gameboard[1][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1gameboard[2][0], "│", player1gameboard[2][1], "│", player1gameboard[2][2], "│", player1gameboard[2][3], "│", player1gameboard[2][4], "│", player1gameboard[2][5], "│", player1gameboard[2][6], "│", player1gameboard[2][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1gameboard[3][0], "│", player1gameboard[3][1], "│", player1gameboard[3][2], "│", player1gameboard[3][3], "│", player1gameboard[3][4], "│", player1gameboard[3][5], "│", player1gameboard[3][6], "│", player1gameboard[3][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1gameboard[4][0], "│", player1gameboard[4][1], "│", player1gameboard[4][2], "│", player1gameboard[4][3], "│", player1gameboard[4][4], "│", player1gameboard[4][5], "│", player1gameboard[4][6], "│", player1gameboard[4][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1gameboard[5][0], "│", player1gameboard[5][1], "│", player1gameboard[5][2], "│", player1gameboard[5][3], "│", player1gameboard[5][4], "│", player1gameboard[5][5], "│", player1gameboard[5][6], "│", player1gameboard[5][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1gameboard[6][0], "│", player1gameboard[6][1], "│", player1gameboard[6][2], "│", player1gameboard[6][3], "│", player1gameboard[6][4], "│", player1gameboard[6][5], "│", player1gameboard[6][6], "│", player1gameboard[6][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", player1gameboard[7][0], "│", player1gameboard[7][1], "│", player1gameboard[7][2], "│", player1gameboard[7][3], "│", player1gameboard[7][4], "│", player1gameboard[7][5], "│", player1gameboard[7][6], "│", player1gameboard[7][7])
    print("")
    
def title():
    #displays name and version of the program
    print("Battleboats V1 | Alexander Dennant")
    print("")

def clear():
    #clear prompt in order to hide from opponent
    os.system("clear")
    
def game(choice, player1refrence, player1gameboard, player2refrence, player2gameboard, p1boatsunk, p2boatsunk, check):
    #P1 Turn
    while p1boatsunk!=5 or p2boatsunk!=5:
        print("----------------------------------------")
        print("")
        print("Player One's Turn")
        print("")
        displaregpb1(player2gameboard)
        print("")
        choice=input("Enter coordinates (in the format 'x,y'): ")
        while check!=True:
            if int(choice[0])>1 or int(choice[0])<8:
                if int(choice[2])>1 or int(choice[2])<8:
                    check=True
                else:
                    print("Error 01: Coordinates have to be between 1 and 8")
                    choice=input("Enter coordinates (in the format 'x,y'): ")
            else:
                print("Error 01: Coordinates have to be between 1 and 8")
                choice=input("Enter coordinates (in the format 'x,y'): ")
        if (player2refrence[(int(choice[0])-1)][(int(choice[2])-1)])!="X":
            print("No Targets Hit")
            (player2gameboard[(int(choice[0])-1)][(int(choice[2])-1)])="O"
        elif (player2refrence[(int(choice[0])-1)][(int(choice[2])-1)])=="X":
            print("Boat Sunk!")
            (player2gameboard[(int(choice[0])-1)][(int(choice[2])-1)])="X"
            p1boatsunk=p1boatsunk+1
        print("")

        #P2 Turn
        print("----------------------------------------")
        print("")
        print("Player Two's Turn")
        print("")
        displaregpb2(player1gameboard)
        print("")
        choice=input("Enter coordinates (in the format 'x,y'): ")
        while check!=True:
            if int(choice[0])>1 or int(choice[0])<8:
                if int(choice[2])>1 or int(choice[2])<8:
                    check=True
                else:
                    print("Error 01: Coordinates have to be between 1 and 8")
                    choice=input("Enter coordinates (in the format 'x,y'): ")
            else:
                print("Error 01: Coordinates have to be between 1 and 8")
                choice=input("Enter coordinates (in the format 'x,y'): ")
        if (player1refrence[(int(choice[0])-1)][(int(choice[2])-1)])!="X":
            print("No Targets Hit")
            (player1gameboard[(int(choice[0])-1)][(int(choice[2])-1)])="O"
        elif (player1refrence[(int(choice[0])-1)][(int(choice[2])-1)])=="X":
            print("Boat Sunk!")
            (player1gameboard[(int(choice[0])-1)][(int(choice[2])-1)])="X"
            p2boatsunk=p2boatsunk+1
        print("")

#variables
board1complete=False
board2complete=False
p1boatsunk=0
p2boatsunk=0
setup=False
choice=0
count=0
check=False
winner=""
turns=0
x=0
y=0

#start
title()
print("Welcome to Battleboats")
print("")
time.sleep(1)
while setup!=True:
    while board1complete!=True:
        while count<5:
            x=random.randint(0,7)
            y=random.randint(0,7)
            if player1refrence[x][y]==" ":
                player1refrence[x][y]="X"
                count=count+1
        board1complete=True
        count=0
    while board2complete!=True:
        while count<5:
            x=random.randint(0,7)
            y=random.randint(0,7)
            if player2refrence[x][y]==" ":
                player2refrence[x][y]="X"
                count=count+1
        board2complete=True
    setup=True

#Display Reference Boards to Players

#player1
print("Displaying Player One's Board in 3 Seconds, hide your display from your opponent")
time.sleep(3)
print("")
displarefpb1(player1refrence)

#resets screen
time.sleep(5)
clear()
title()

#player2
print("Displaying Player Two's Board in 3 Seconds, hide your display from your opponent")
time.sleep(3)
print("")
displarefpb2(player2refrence)

#resets screen
time.sleep(5)
clear()
title()

#Game
game(choice, player1refrence, player1gameboard, player2refrence, player2gameboard, p1boatsunk, p2boatsunk, check)

#End
if p1boatsunk>p2boatsunk:
    print("Well Done Player One! You Won")
else:
    print("Well Done Player Two! You Won")