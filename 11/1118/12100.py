from collections import deque

N = int(input())
q = deque()

board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def get(i,j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j] = 0


def merge(i,j,di,dj):
    while q :
        x = q.popleft()
        if not board[i][j] : board[i][j] = x
        elif board[i][j] == x : 
            board[i][j] += x
            i, j = i + di, j + dj
        else :
            i, j = i+di, j+dj
            board[i][j] = x

def move(m):
    if m == 0 : # 위
        for j in range(N):
            for i in range(N):
                get(i,j)
            merge(0,j,1,0)
    elif m == 1 : #아래
        for j in range(N):
            for i in range(N-1, -1, -1):
                get(i, j)
            merge(N-1,j,-1, 0)
 
    elif m == 2 : #왼쪽
        for i in range(N):
            for j in range(N):
                get(i,j)
            merge(i, 0, 0, 1) 
    else : #오른쪽 
        for i in range(N):
            for j in range(N-1, -1, -1):
                get(i,j)
            merge(i, N-1, 0, -1)


def dfs(count):
    global board, answer
    if count == 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return
    b = [x[:] for x in board]
    for i in range(4):
        move(i)
        dfs(count + 1)
        board = [x[:] for x in b]

dfs(0)
print(answer)
