import math

def is_valid(sudoku, row, col, num, n):
    for i in range(n*n):
        if sudoku[row][i] == num:
            return False
        if sudoku[i][col] == num: 
            return False

    start_row, start_col = n * (row // n), n * (col // n)
    for i in range(n):
        for j in range(n):
            if sudoku[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(sudoku, n):
    for i in range(n*n):
        for j in range(n*n):
            if sudoku[i][j] == 0:
                for num in range(1, n*n + 1):
                    if is_valid(sudoku, i, j, num, n):
                        sudoku[i][j] = num
                        if solve_sudoku(sudoku, n):
                            return True
                        sudoku[i][j] = 0
                return False
    return True

def display_sudoku(sudoku):
    for row in sudoku:
        print(*row)

sudoku = []

n = int(math.sqrt(int(input("sudoku dimensions >> "))))

for i in range(n*n):
    print("row", i + 1, ">> ", end="")
    row = list(map(int, input().split()))
    sudoku.append(row)

solve_sudoku(sudoku, n)
display_sudoku(sudoku)
