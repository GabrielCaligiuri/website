import random
import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_full_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_diagonal_blocks(board)
    solve(board)
    return board

def fill_diagonal_blocks(board):
    for i in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for row in range(3):
            for col in range(3):
                board[i + row][i + col] = nums.pop()

def hide_squares(board, shown):
    total = 81
    to_hide = total - shown
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    for i in range(to_hide):
        row, col = positions[i]
        board[row][col] = 0
    return board

def generate_sudoku():
    shown_squares = 17
    board = generate_full_board()
    puzzle = [row[:] for row in board]  # Copy
    hide_squares(puzzle, shown_squares)
    return puzzle

def display_board(board):
    for widget in grid_frame.winfo_children():
        widget.destroy()

    for i in range(9):
        for j in range(9):
            value = board[i][j]
            cell = tk.Label(grid_frame, text=str(value) if value != 0 else '', width=2, height=1, font=("Helvetica", 18), borderwidth=1, relief="solid")
            cell.grid(row=i, column=j, padx=1, pady=1)

def generateBoard():
    puzzle = generate_sudoku()
    display_board(puzzle)

# GUI setup
root = tk.Tk()
root.title("Sudoku Generator")

frame = tk.Frame(root)
frame.pack(pady=10)

grid_frame = tk.Frame(root)
grid_frame.pack(pady=10)

generateBoard()

root.mainloop()
