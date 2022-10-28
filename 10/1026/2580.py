import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

blank = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0 : blank.append([i,j])

def check_row(row, n):
    for i in range(9):
        if sudoku[row][i] == n : return False
    return True

def check_col(col, n):
    for i in range(9):
        if sudoku[i][col] == n : return False
    return True

def check_d(row, col, n):
    row_ = row // 3
    col_ = col // 3
    for i in range(row_ * 3, (row_ + 1) * 3):
        for j in range(col_ * 3, (col_ + 1) * 3):
            if sudoku[i][j] == n : return False
    return True

def dfs(depth):
    if depth == len(blank) : 
        for i in range(9):
            print(' '.join(map(str, sudoku[i])))
        exit()
    row = blank[depth][0]
    col = blank[depth][1]
    for i in range(1, 10):   
        if check_row(row, i) and check_col(col, i) and check_d(row, col, i) : 
            sudoku[row][col] = i
            dfs(depth+1)
            sudoku[row][col] = 0
        
dfs(0)