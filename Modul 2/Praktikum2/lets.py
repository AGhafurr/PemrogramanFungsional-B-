import random

def CreateBoard(width, height):
    board = [['-' for _ in range(width)] for _ in range(height)]
    return board
    
def InitializeBoard(board, width, height):
    board = CreateBoard(width, height)
    player_x, player_y = random.randint(0, width - 1), random.randint(0, height - 1)
    goal_x, goal_y = random.randint(0, width - 1), random.randint(0, height - 1)
    board[player_y][player_x] = 'A'
    board[goal_y][goal_x] = 'O'
    return board, player_x, player_y, goal_x, goal_y

def PrintBoard(board):
    for row in board:
        print(' '.join(row))

def MoveBoard(board, PlayerX, PlayerY, move):
    width = len(board[0])
    height = len(board)

    if move == 'A' and PlayerX > 0:
        board[PlayerY][PlayerX], board[PlayerY][PlayerX - 1] = board[PlayerY][PlayerX - 1], board[PlayerY][PlayerX]
        PlayerX -= 1
    elif move == 'D' and PlayerX < width - 1:
        board[PlayerY][PlayerX], board[PlayerY][PlayerX + 1] = board[PlayerY][PlayerX + 1], board[PlayerY][PlayerX]
        PlayerX += 1
    elif move == 'W' and PlayerY > 0:
        board[PlayerY][PlayerX], board[PlayerY - 1][PlayerX] = board[PlayerY - 1][PlayerX], board[PlayerY][PlayerX]
        PlayerY -= 1
    elif move == 'S' and PlayerY < height - 1:
        board[PlayerY][PlayerX], board[PlayerY + 1][PlayerX] = board[PlayerY + 1][PlayerX], board[PlayerY][PlayerX]
        PlayerY += 1

    return board, PlayerX, PlayerY

def TextSambutan():
    print("~~ Selamat datang di permainan board game Pemrograman Fungsional !!")
    print("------------------------------------------------------------")
    print("Anda (A) dapat berjalan secara horizontal dan vertikal untuk menuju target (O)")
    print("Gunakan keyboard ASDW untuk bergerak")
    print("------------------------------------------------------------")
    print("~~ Selamat Bermain ~~")

def main():
    while True:
        TextSambutan()
        width = int(input("Enter the Board width: "))
        height = int(input("Enter the Board height: "))

        board, PositionX, PositionY, GoalX, GoalY = InitializeBoard(CreateBoard(width, height), width, height)    
        PrintBoard(board)

        while True:
            choise = input("New Position: ")
            if choise.lower() == 'y':
                board, PositionX, PositionY, GoalX, GoalY = InitializeBoard(CreateBoard(width, height), width, height)
                PrintBoard(board)
            else:
                break   
            
        print("Let's play... This is your game board")

        while True:
            PrintBoard(board)
            moves = input("What are your moves = ").upper()

            if 'Q' in moves:
                break

            for move in moves:
                board, PositionX, PositionY = MoveBoard(board, PositionX, PositionY, move)

                if PositionX != GoalX or PositionY != GoalY:
                    print("You Lose!")

                elif PositionX == GoalX and PositionY == GoalY:
                    PrintBoard(board)
                    print("You Win!!")
                    break

        close = input("Wanna try again? (Y/N): ").upper()
        if close == 'N':
            break

if __name__ == "__main__":
    main()
