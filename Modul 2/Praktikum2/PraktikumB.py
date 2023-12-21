import random

# 1. Buat board matrix dengan lebar sesuai dengan inputan dari user. Kalian bisa memanfaatkan list comprehension untuk membuat board matrix ini.
create_board = lambda width, height: [['-' for _ in range(width)] for _ in range(height)]

# Terdapat sebuah bidak (simbol A) yang dapat berjalan secara horizontal dan vertikal, serta sebuah goals (simbol O) sebagai target/tujuan permainan.
def Bidak(board, width, height):
    positionX, positionY = random.randint(0, width - 1), random.randint(0, height - 1)
    goalX, goalY = random.randint(0, width - 1), random.randint(0, height - 1)
    board[positionY][positionX] = 'A'
    board[goalY][goalX] = 'O'
    return board, positionX, positionY, goalX, goalY

def PrintBoard(board):
    for row in board:
        print(' '.join(row))

def MoveBoard(board, positionX, positionY, move):
    width = len(board[0])
    height = len(board)

    #pergerakan user
    if move == 'A' and positionX > 0:
        board[positionY][positionX] = '-'
        positionX -= 1
        board[positionY][positionX] = 'A'
    elif move == 'D' and positionX < width - 1:
        board[positionY][positionX] = '-'
        positionX += 1
        board[positionY][positionX] = 'A'
    elif move == 'W' and positionY > 0:
        board[positionY][positionX] = '-'
        positionY -= 1
        board[positionY][positionX] = 'A'
    elif move == 'S' and positionY < height - 1:
        board[positionY][positionX] = '-'
        positionY += 1
        board[positionY][positionX] = 'A'

    return board, positionX, positionY

def TextSambutan():
    print("~~ Selamat datang di permainan board game Pemrograman Fungsional !!")
    print("------------------------------------------------------------")
    print("Anda (A) dapat berjalan secara horizontal dan vertikal untuk menuju target (O)")
    print("Gunakan keyboard ASDW untuk bergerak")
    print("------------------------------------------------------------")
    print("~~ Selamat Bermain ~~")

def main():
    TextSambutan()
    while True:
        width = int(input("Enter the Board width: "))
        height = int(input("Enter the Board height:"))

        board, positionX, positionY, GoalX, GoalY = Bidak(create_board(width, height), width, height)

        PrintBoard(board)

        perhitunganReset = 0

        #new Board
        while True:
            choice = input("New Position (3 Chance to Change Position): ").format(3-perhitunganReset)
            if choice.lower() == 'y':
                if perhitunganReset < 3:
                    board, positionX, positionY, GoalX, GoalY = Bidak(create_board(width, height), width, height)
                    perhitunganReset +=1
                    PrintBoard(board)
                else:
                    print("Anda sudah pada batas 3 kali reset Board!")
                    break
            else:
                break

        print("Let's Play....")
        print("This Your Game Board!")

        while True:
            PrintBoard(board)

            #Q keluar
            Moves = input("What are your moves = ").upper()
            if 'Q' in Moves:
                break
            
            #Perulangan buat sekali jalan
            for move in Moves:
                board, positionX, positionY = MoveBoard(board, positionX, positionY, move)

            if positionX != GoalX and positionY != GoalY:
               print("You Lose!")
               break
            elif positionX == GoalX and positionY == GoalY:
               PrintBoard(board)
               print("You Win!!")
               break

        close = input("Wanna try again? (Y/N): ").upper()
        if close == 'N':
            break

if __name__ == "__main__":
    main()
