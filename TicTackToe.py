import pprint
import random

def print_formatted(data):
    """Pretty prints the given data."""
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)

def main():
    """Main entry point for the Tic-Tac-Toe game."""
    print_formatted("Welcome to Tic-Tac-Toe!")
    userInterface(createBoard())

def createBoard():
    # Board is 3X3
    board = [['.' for i in range(3)] for j in range(3)]
    return board

def checkBoard(board, x, y):
    if board[x][y] == ".":
        return True
    return False

def setBoard(board, x, y, val):
    if checkBoard(board, x, y):
        board[x][y] = val
    else:
        print_formatted(f"{x},{y} spot not available!")

def boardPrint(board):
    header_row = ['0', '1', '2']
    i = 0
    print_formatted(f"    {str.join(',   ', header_row)}")
    for row in board:
        print_formatted(f"{i} {row}")
        i += 1

def checkWin(board, val):
    # Left diagonal of same values
    if board[0][0] == val and board[1][1] == val and board[2][2] == val:
        print_formatted(f"Player {val} has won!")
        return True
    # Right diagonal of same values
    if board[0][2] == val and board[1][1] == val and board[2][0] == val:
        print_formatted(f"Player {val} has won!")
        return True
    # Check 3 rows
    if board[0][0] == val and board[0][1] == val and board[0][2] == val:
        print_formatted(f"Player {val} has won!")
        return True
    if board[1][0] == val and board[1][1] == val and board[1][2] == val:
        print_formatted(f"Player {val} has won!")
        return True
    if board[2][0] == val and board[2][1] == val and board[2][2] == val:
        print_formatted(f"Player {val} has won!")
        return True
    # Check 3 cols
    if board[0][0] == val and board[1][0] == val and board[2][0] == val:
        print_formatted(f"Player {val} has won!")
        return True
    if board[0][1] == val and board[1][1] == val and board[2][1] == val:
        print_formatted(f"Player {val} has won!")
        return True
    if board[0][2] == val and board[1][2] == val and board[2][2] == val:
        print_formatted(f"Player {val} has won!")
        return True

    return False

def setRandomCoordinates(board):
    x = random.randint(0,2)
    y = random.randint(0,2)

    while not checkBoard(board, x, y):
        x = random.randint(0, 2)
        y = random.randint(0, 2)

    setBoard(board,x,y,'O')

def isBoardFull(board):
    for i in  range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                return False
    return True


def userInterface(board):
    boardPrint(board)
    while not checkWin(board, 'O') and not checkWin(board, 'X'):

        # User makes move first.
        usr_line = input("User Move!, select x,y coordinates\n")
        usr_coordinates = [int(x) for x in usr_line.split(',')]
        breakout = False

        while not breakout:
            if checkBoard(board, usr_coordinates[0], usr_coordinates[1]):
                setBoard(board, usr_coordinates[0], usr_coordinates[1], 'X')
                print_formatted("User made move!")
                boardPrint(board)
                breakout = True
            else:
                usr_line = input("x,y coordinates taken!, chose another location\n")
                usr_coordinates = [int(x) for x in usr_line.split(',')]

        if checkWin(board, 'X'):
            break

        if isBoardFull(board):
            print_formatted("Draw!")
            break

        # Now Computer makes move
        setRandomCoordinates(board)
        print_formatted("Computer Made move!")
        boardPrint(board)

if __name__ == "__main__":
    main()
