board=["-","-","-","-","-","-","-","-","-"]

currentplayer='X'
winner=None
gamerunning=True

def printboard(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print("----------")
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print("----------")
    print(f'{board[6]} | {board[7]} | {board[8]}')

def player_input(board):
    global currentplayer
    inp = int(input("Sheiyvane ricxvi 1-9 "))
    if board[inp-1]=="-" and inp<=9 and inp>=1:
        board[inp-1]=currentplayer
        switch_player()

def switch_player():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    elif currentplayer == "O":
        currentplayer = "X"

def check_horizont(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner = board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner = board[6]
        return True

def check_diag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner = board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner = board[2]
        return True
    
def check_vert(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner = board[0]
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner = board[1]
        return True
    elif board[2]==board[5]==board[8] and board[8]!="-":
        winner = board[8]
        return True

def check_win(board):
    global gamerunning
    if check_diag(board) or check_horizont(board) or check_vert(board):
        print(winner)
        printboard(board)
        gamerunning = False

def check_tie(board):
    global gamerunning
    global winner
    if "-" not in board and winner == None:
        gamerunning=False
        print("Tie")

while gamerunning:
    printboard(board)
    player_input(board)
    check_win(board)
    check_tie(board)

    
