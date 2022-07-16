from pprint import pprint


def find_empty(sudoku):
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                return r, c
    return None, None

def is_valid(sudoku, guess, row, column):
    row_val = sudoku[row]
    if guess in row_val:
        return False

    col_val = [sudoku[i][column] for i in range(9)]
    if guess in col_val:
        return False

    row_start = (row // 3) * 3
    col_start = (column // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if sudoku[r][c] == guess:
                return False

    return True


def solve(sudoku):
    row, column = find_empty(sudoku)
    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(sudoku, guess, row, column):
            sudoku[row][column] = guess
            if solve(sudoku):
                return True
        sudoku[row][column] = 0
    return False

if __name__ == '__main__':
    example_board = sudoku = [
    [0, 8, 0, 0, 9, 0, 7, 5, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 7, 0, 0, 0, 0, 6],
    [3, 0, 0, 1, 0, 0, 8, 7, 0],
    [0, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
    [8, 0, 0, 2, 0, 0, 1, 3, 0],
    [0, 9, 0, 0, 0, 4, 0, 0, 0]
]
    print(solve(example_board))
    pprint(example_board)
