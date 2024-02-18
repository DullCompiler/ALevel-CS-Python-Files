#Refrence
        # r  c
    #board[0][0]

#Winning Combinations
    #[0][0] [0][1] [0][2]
    #[1][0] [1][1] [1][2]
    #[2][0] [2][1] [2][2]

    #[0][0] [1][0] [2][0]
    #[0][1] [1][1] [2][1]
    #[0][2] [1][2] [2][2]

    #[0][0] [1][1] [2][2]
    #[0][2] [1][1] [2][0]

#Variables
board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

player=0
win=False
choice=0

def displayboard(board):
    print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
    print(" ───┼───┼───")
    print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
    print(" ───┼───┼───")
    print(" ", board[2][0], "│", board[2][1], "│", board[2][2])
    
def winning(board, win):
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"):
        win=True
    elif (board[0][0] == "X" and board[1][1] == "X" and board[2][0] == "X") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
        win=True
    elif (board[0][0] == "X" and board[1][1] and board[2][2] == "X") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        win=True
    elif (board[0][0] == "O" and board[0][2] == "O") or (board[1][0] and board[1][1] == "O" and board[1][2] == "O") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
        win=True
    elif (board[0][0] == "O" and board[1][1] == "O" and board[2][0] == "O") or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        win=True
    elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        win=True
    else:
        win=False
    return win

def player1choice():
    choice=int(input("Where do you want to place your piece?: "))
    if choice==1:
        board[0][0]="X"
    if choice==2:
        board[0][1]="X"
    if choice==3:
        board[0][2]="X"
    if choice==4:
        board[1][0]="X"
    if choice==5:
        board[1][1]="X"
    if choice==6:
        board[1][2]="X"
    if choice==7:
        board[2][0]="X"
    if choice==8:
        board[2][1]="X"
    if choice==9:
        board[2][2]="X"

def player2choice():
    choice=int(input("Where do you want to place your piece?: "))
    if choice==1:
        board[0][0]="O"
    if choice==2:
        board[0][1]="O"
    if choice==3:
        board[0][2]="O"
    if choice==4:
        board[1][0]="O"
    if choice==5:
        board[1][1]="O"
    if choice==6:
        board[1][2]="O"
    if choice==7:
        board[2][0]="O"
    if choice==8:
        board[2][1]="O"
    if choice==9:
        board[2][2]="O"
        
while win==False:
    player="One"
    print("Player One's Turn")
    displayboard(board)
    player1choice()
    win = winning(board, win)
    if win==True:
        break
    player="Two"
    print("Player Two Choice")
    displayboard(board)
    player2choice()
    win = winning(board, win)
    print("")

print("")
print("Game over | Player", player, "won!")
displayboard(board)