import math

board = [' '] * 9
lines = [(0,1,2), (3,4,5), (6,7,8),
         (0,3,6), (1,4,7), (2,5,8),
         (0,4,8), (2,4,6)]
nodes = 0

# Check winner
def win(p):
    return any(
        all( board[i] == p for i in line)
        for line in lines
        )

# Minimax with Alpha-Beta Pruning
def minimax(isMax, alpha, beta, d=0):
    global nodes
    nodes += 1

    if win('O'): return 10 - d
    if win('X'): return d - 10
    if ' ' not in board: return 0

    if isMax:
        best = -math.inf
        p = 'O'
    else:
        best = math.inf
        p = 'X'

    for i in range(9):
        if board[i] == ' ':
            board[i] = p
            score = minimax(not isMax, alpha, beta, d+1)
            board[i] = ' '

            if isMax:
                best = max(best, score)
                alpha = max(alpha, best)
            else:
                best = min(best, score)
                beta = min(beta, best)

            if alpha >= beta:
                break

    return best

# Find computer's best move
def computer_move():
    global nodes
    nodes = 0
    best, move = -math.inf, None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False, -math.inf, math.inf, 1)
            board[i] = ' '

            if score > best:
                best, move = score, i

    print("Nodes explored:", nodes)
    return move

# Display board
def display():
    for i in range(0, 9, 3):
        print(' | '.join(board[i:i+3]))
    print()

# Main game
while True:
    display()

    p = int(input("Enter position (1-9): ")) - 1

    if p not in range(9) or board[p] != ' ':
        print("Invalid move!")
        continue

    board[p] = 'X'

    if win('X'):
        display()
        print("You win!")
        break

    if ' ' not in board:
        display()
        print("Draw!")
        break

    move = computer_move()
    board[move] = 'O' # type: ignore

    if win('O'):
        display()
        print("Computer wins!")
        break

    if ' ' not in board:
        display()
        print("Draw!")
        break