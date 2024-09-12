#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False
    # Check the diagonal (top-left to bottom-right)
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False
    # Check the diagonal (top-right to bottom-left)
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i] == j:
            return False
    return True


def solve_nqueens(N):
    """Solve the N Queens problem and print all solutions."""
    def backtrack(row, board):
        """Backtracking function to place queens row by row."""
        if row == N:
            # A solution is found, print it
            print([[i, board[i]] for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col  # Place queen
                backtrack(row + 1, board)  # Move to next row
                board[row] = -1  # Backtrack (remove the queen)

    board = [-1] * N  # Initialize the board with no queens placed
    backtrack(0, board)


if __name__ == "__main__":
    # Handle command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(N)
