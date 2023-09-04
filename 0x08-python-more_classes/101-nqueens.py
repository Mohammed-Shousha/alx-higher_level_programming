#!/usr/bin/python3
"""A program to find all solutions to the nqueens problem"""


def nqueens(n):
    """A function to find all solutions to the nqueens problem"""
    board = [[0] * n for _ in range(n)]
    solve(board, 0, n)


def solve(board, col, n):
    """A recursive function to solve the nqueens problem"""
    if col == n:
        print_board(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve(board, col + 1, n) or res
            board[i][col] = 0

    return res


def is_safe(board, row, col, n):
    """A function to check if a queen can be placed on board[row][col]"""
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

        if row - i >= 0 and col - i >= 0 and board[row-i][col-i] == 1:
            return False

        if row + i < n and col - i >= 0 and board[row+i][col-i] == 1:
            return False

    return True


def print_board(board):
    """A function to print the board"""
    queens = [[i, j] for i in range(len(board))
              for j in range(len(board)) if board[i][j] == 1]
    print(queens)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    n = sys.argv[1]

    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(int(sys.argv[1]))
