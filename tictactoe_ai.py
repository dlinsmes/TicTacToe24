
#variables don't need to be declared with types
#board is a list
board = []

piece = "o"
moveRow = -1
moveCol = -1



def main():
    setupBoard()
    printBoard()

    while not winner() and not tie():
        changePiece()
        makeMove()
        printBoard()

    # use global if you're changing the variable (maybe?)
    if winner():
        print(piece + " wins!")
    else:
        print("tie game")


def setupBoard():
    #for loop that iterates 0-1-2
    for i in range(3):
        row = []
        for j in range(3):
            row.append("_")
        board.append(row)

def printBoard():
    #for each loop
    for row in board:
        # print(row)
        line = ""
        for thing in row:
            line += thing + "  "
        print(line)
    print()

def winner():
    global moveRow
    global moveCol

    rowCount = 0
    colCount = 0
    d1Count = 0
    d2Count = 0
    for i in range(3):
        # ++ doesn't work in python
        if board[moveRow][i] == piece:
            rowCount += 1
        if board[i][moveCol] == piece:
            colCount += 1
        if board[i][i] == piece:
            d1Count += 1

        #len(list) gives the length; len of a 2d list is the number of rows
        if board[i][len(board)-1-i] == piece:
            d2Count += 1

    if rowCount == 3 or colCount == 3 or d1Count == 3 or d2Count == 3:
        return True

    return False

def tie():
    for row in board:
        for thing in row:
            if thing == "_":
                return False
    return True
def changePiece():
    # specify you're using a global (class) variable that is shared by
    # the whole file
    global piece
    if piece == "o":
        piece = "x"
    else:
        piece = "o"

def makeMove():
    global moveRow
    global moveCol

    print(piece + "'s turn")
    # get inputs for row and col

    #human player is x
    if piece == "x":

        #input defaults to Strings, need to cast to int
        moveRow = int(input("Enter row: "))
        moveCol = int(input("Enter col: "))

        while moveRow < 0 or moveRow >= 3 or moveCol < 0 or moveCol >= 3 \
                or board[moveRow][moveCol] != "_":
            print("invalid coordinate")
            moveRow = int(input("Enter row: "))
            moveCol = int(input("Enter col: "))

    else:
        moveRow, moveCol = ai_turn()

    board[moveRow][moveCol] = piece

def ai_turn():
    row = -1
    col = -1

    #your logic for the move row/col goes here

    #python functions can return multiple values
    return row, col


#need to call functions AFTER they're defined
main()