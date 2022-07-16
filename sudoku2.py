puzzle = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
""" Print sudoku in nice readable format"""
def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(sudoku[i][j]))
            else:
                print(str(sudoku[i][j]) + " ", end="")

""" Find empty cell to fill in"""
def find_empty(sudoku):
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                return r, c
    return None

"""pos is position of cell that is tuple (r, c)"""
def is_valid(sudoku, num, pos):
    """ Check row"""
    for c in range(len(sudoku[0])):
        if sudoku[pos[0]][c] == num and pos[1] != c:
            return False
    """ Check column"""
    for r in range(len(sudoku)):
        if sudoku[r][pos[1]] == num and pos[0] != r:
            return False
    """ Check square of 3x3"""
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sudoku[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(sudoku):
    """ Find empty cell first , if no empty cell, then puzzle is solved"""
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        r, c = find

    for num in range(1, 10):
        if is_valid(sudoku, num, (r, c)):
            sudoku[r][c] = num
            """ after add valid number, do the same thing with new puzzle"""
            if solve(sudoku):
                return True
            """ if not num added is not valid, empty (0) and go back (backtrack)"""
            sudoku[r][c] = 0

    return False
    # """ It is not valid puzzle"""

print_sudoku(puzzle)
solve(puzzle)
print("--------------------")
print("--------------------")
print_sudoku(puzzle)










