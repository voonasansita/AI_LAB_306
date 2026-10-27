def print_board(board):
    for row in board:
        print(" ".join(row))
    print()  # Adds an empty line between different solutions

def is_safe(board, row, col, n):
    # Check vertical column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n, solution_tracker):
    # Base case: All queens are placed successfully
    if row == n:
        solution_tracker['count'] += 1
        print(f"Solution #{solution_tracker['count']}:")
        print_board(board)
        return  # Return to find more solutions

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'

            # Recursively try placing queens in the next rows
            solve(board, row + 1, n, solution_tracker)

            board[row][col] = '.'  # Backtrack

# Define N here (e.g., 8, 8)
N = 8
board = [['.' for _ in range(N)] for _ in range(N)]

# Dictionary to track the total count across recursive calls
tracker = {'count': 0}

solve(board, 0, N, tracker)

print(f"Total number of possible solutions for {N}-Queens: {tracker['count']}")
