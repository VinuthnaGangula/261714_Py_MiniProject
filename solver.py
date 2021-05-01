# Implementation of Sudoku puzzle solver
from pprint import pprint


# Returns the values of row and column for the next empty cell
def next_empty_cell(puzzle):
    # let the empty cells of puzzle be represented as '-1'
    for p in range(9):
        for q in range(9):
            if puzzle[p][q] == -1:
                return p, q

    # If the puzzle is completely filled.
    return None, None


# Checks the validity of a number to be placed in a cell.
def valid_guess(puzzle, row_val, col_val, val):
    # Check if the value is already in the row 'row_val'
    r_list = puzzle[row_val]
    if val in r_list:
        return False

    # Check if the value is already present in the column 'col_val'
    c_list = [puzzle[p][col_val] for p in range(9)]
    if val in c_list:
        return False

    # Check if the value is present in its corresponding 3x3 matrix.
    # Evaluate the start row index of the matrix
    r = (row_val // 3) * 3
    # Evaluate the start column index of the matrix
    c = (col_val // 3) * 3

    for p in range(r, r + 3):
        for q in range(c, c + 3):
            if val == puzzle[p][q]:
                return False

    # If the value is not found, then it can be placed in the cell.
    return True


def solve(grid):
    # Get the next empty cell to be filled.
    row, col = next_empty_cell(grid)

    # Solved if all rows and columns are filled.
    if row is None:
        return True

    # If not, try to make a guess.
    for guess in range(1, 10):
        # Check validity of the guess.
        if valid_guess(grid, row, col, guess):
            grid[row][col] = guess

            if solve(grid):
                return True

        # If the guess is not valid, we must try another number.
        grid[row][col] = -1

    # If no value from 1 to 9 is valid, then the Sudoku is unsolvable or incorrect.
    return False


def validate_puzzle(puzzle):
    # Check if the incomplete puzzle is valid or not.
    # Check for duplicates in row.
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != -1:
                if puzzle[r][c] in puzzle[(c + 1):] or puzzle[r][c] == 0 or puzzle[r][c] < 0:
                    return False
    # Check for duplicates in column.
    for p in range(9):
        col = [puzzle[p][q] for q in range(9)]
        for c in range(9):
            if col[c] != -1:
                if col[c] in col[(c+1):]:
                    return False

    return True


def display(puzzle):
    # To display the sudoku.
    for i in range(len(puzzle)):
        if i % 3 == 0:
            print("+---------+---------+---------+")

        for j in range(len(puzzle[0])):
            if j % 3 == 0:
                print("\b|", end=" ")

            print(str(puzzle[i][j])+" ", end=" ")
        print("\b|")
    print("+---------+---------+---------+")


if __name__ == "__main__":
    choice = int(input('Enter 1 to enter your puzzle or Enter 2 to choose a random puzzle: '))
    sudoku_example = []
    if choice != 1:
        sudoku_example = [
            [1, -1, -1, 3, 8, -1, -1, 5, 7],
            [-1, -1, 3, -1, 4, 6, 1, -1, -1],
            [2, 8, 9, -1, 5, -1, -1, -1, -1],

            [6, -1, 5, 8, -1, -1, 2, -1, 4],
            [-1, 9, -1, -1, -1, -1, 7, 8, 1],
            [-1, 4, 7, 2, -1, 3, -1, -1, 9],

            [5, 3, 1, -1, 9, -1, 4, -1, 2],
            [-1, -1, -1, 1, 3, 7, -1, 9, 5],
            [-1, -1, 8, 4, -1, -1, 6, -1, -1]
        ]
    else:
        print("Please enter your puzzle in the displayed format: ")
        for i in range(9):
            for j in range(9):
                print((i + j) % 10, end=" ")
            print()
        print("Enter -1 to represent empty cells in the puzzle.")
        print("Enter your puzzle: ")
        for i in range(9):
            temp_list = list(map(int, input().split()))
            sudoku_example.append(temp_list)

    if validate_puzzle(sudoku_example):
        print("\nThe puzzle chosen to be solved: ")
        for i in range(9):
            for j in sudoku_example[i]:
                print(str(j), end=" ")
            print()
        print()
        if solve(sudoku_example):
            print("Here is the solved puzzle!")
            display(sudoku_example)
        else:
            print("The puzzle is invalid! Sorry, It can't be solved.")
    else:
        print("The puzzle is invalid! Sorry, It can't be solved.")
