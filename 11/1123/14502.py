from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

zero_list = []
two_list = []
res = []

dx, dy = (1, -1, 0, 0), (0,0,1,-1) 

def count(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not board[i][j] : cnt += 1
    res.append(cnt)

def move(x, y, dm, dn):
    if x + dm < 0 or x + dm > N -1 or y+ dn < 0 or y + dn > M - 1 : return
    x, y = x+dm, y+dn
    if board[x][y] == 1 or board[x][y] == 2 : return
    if board[x][y] == 0 : board[x][y] = 2
    for i in range(4):
        move(x, y, dx[i], dy[i])


for i in range(N):
    for j in range(M):
        if not board[i][j]:
            zero_list.append((i,j)) # 0 list ㅁㅏㄴ드ㄹ기
        if board[i][j] == 2 : two_list.append((i,j))


for l in list(combinations(zero_list, 3)):
    b = [x[:] for x in board]
    for j in range(3):
        board[l[j][0]][l[j][1]] = 1
    for two in two_list :
        for d in range(4):
            move(two[0], two[1], dx[d], dy[d])
    count(board)
    board = [x[:] for x in b]

print(max(res))