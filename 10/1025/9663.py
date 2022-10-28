def check_valid(chess, row, col) :
    for i in range(row):
        if chess[i] == col or abs(i - row) == abs(chess[i] - col) : return False
    return True

def n_queen(row) :
    global cnt
    if row == N : cnt += 1; return
    for i in range(1, N + 1):
        if used[i] : continue
        if check_valid(chess, row, i) :
            used[i] = 1 
            chess[row] = i
            n_queen(row+1)
            used[i] = 0

N = int(input())
chess =[0] * N
used = [0] * (N + 1)
cnt = 0

n_queen(0)
print(cnt)




