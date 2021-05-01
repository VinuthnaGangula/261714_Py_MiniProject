# Implementation of Sudoku Generator.

# Check the validity.
def check_valid(grid, r, c, n):
    valid = True
    # check row and column
    for x in range(9):
        if n == grid[x][c]:
            valid = False
            break
    for y in range(9):
        if n == grid[r][y]:
            valid = False
            break
    row_section = (r // 3) * 3
    col_section = (c // 3) * 3
    for x in range(3):
        for y in range(3):
            if n == grid[row_section + x][col_section + y]:
                valid = False
                break
    return valid

def generate_puzzle():
    import random

    # Initialize puzzle with value '-1' in all cells.
    puzzle = [[-1 for x in range(9)] for y in range(9)]

    # Generate the puzzle using random.
    for i in range(20):
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        while not check_valid(puzzle, row, col, num) or puzzle[row][col] != -1:
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        puzzle[row][col] = num
    return puzzle


if __name__ == "__main__":
    # Display the generated puzzle.
    sudoku_ = generate_puzzle()
    for r in range(9):
        for c in range(9):
            print(sudoku_[r][c], end=" ")
        print()
