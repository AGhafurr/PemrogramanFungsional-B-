import random

def create_board(width, height):
    return [['-' for _ in range(width)] for _ in range(height)]

def initialize_board(board, width, height):
    board = create_board(width, height)
    player_x, player_y = random.randint(0, width - 1), random.randint(0, height - 1)
    goal_x, goal_y = random.randint(0, width - 1), random.randint(0, height - 1)
    board[player_y][player_x] = 'A'
    board[goal_y][goal_x] = 'O'
    return board, player_x, player_y, goal_x, goal_y

def print_board(board):
    for row in board:
        print(' '.join(row))

def move(board, player_x, player_y, move):
    width = len(board[0])
    height = len(board)

    if move == 'A' and player_x > 0:
        board[player_y][player_x], board[player_y][player_x - 1] = board[player_y][player_x - 1], board[player_y][player_x]
        player_x -= 1
    elif move == 'D' and player_x < width - 1:
        board[player_y][player_x], board[player_y][player_x + 1] = board[player_y][player_x + 1], board[player_y][player_x]
        player_x += 1
    elif move == 'W' and player_y > 0:
        board[player_y][player_x], board[player_y - 1][player_x] = board[player_y - 1][player_x], board[player_y][player_x]
        player_y -= 1
    elif move == 'S' and player_y < height - 1:
        board[player_y][player_x], board[player_y + 1][player_x] = board[player_y + 1][player_x], board[player_y][player_x]
        player_y += 1

    return board, player_x, player_y

def main():
    width = int(input("Enter the Board width: "))
    height = int(input("Enter the Board height: "))

    board, player_x, player_y, goal_x, goal_y = initialize_board(create_board(width, height), width, height)

    print("Let's play... This is your game board")
    

    while True:
        print_board(board)
        move_direction = input("What is your move (ASDW/Q)? ").upper()

        if move_direction == 'Q':
            break

        board, player_x, player_y = move(board, player_x, player_y, move_direction)

        if player_x == goal_x and player_y == goal_y:
            print("Congratulations! You won.")
            break

        if player_x != goal_x or player_y != goal_y:
            print("Sorry, you lost. The goal was not reached.")

if __name__ == "__main__":
    main()
