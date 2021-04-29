# Implementation of Sudoku puzzle solver
from pprint import pprint


# Returns the values of row and column for the next empty cell
def next_empty_cell(puzzle):
    # let the empty cells of puzzle be represented as '-1'
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1:
                return i, j

    # If the puzzle is completely filled.
    return None, None


# Checks the validity of a number to be placed in a cell.
def valid_guess(puzzle, row_val, col_val, val):
    # Check if the value is already in the row 'row_val'
    r_list = puzzle[row_val]
    if val in r_list:
        return False

    # Check if the value is already present in the column 'col_val'
    c_list = [puzzle[i][col_val] for i in range(9)]
    if val in c_list:
        return False

    # Check if the value is present in its corresponding 3x3 matrix.
    # Evaluate the start row index of the matrix
    r = (row_val // 3) * 3
    # Evaluate the start column index of the matrix
    c = (col_val // 3) * 3

    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if val == puzzle[i][j]:
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


def display(puzzle):
    # To display the sudoku.
    row = 0
    for i in range(13):
        col = 0
        for j in range(13):
            if i % 4 == 0:
                print("+ - - - + - - - + - - - +")
                # TODO!!


if __name__ == "__main__":
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
    print(solve(sudoku_example))
    display(sudoku_example)
