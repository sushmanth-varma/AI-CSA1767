N = 8
def print_solution(board):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i] == j else ".", end=" ")
        print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row):
    if row == N:
        print_solution(board)
        print()
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1)
            board[row] = -1

board = [-1] * N
solve_n_queens(board, 0)
