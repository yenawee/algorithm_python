import sys
from collections import deque
input = sys.stdin.readline
N , M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

q = deque()
def init():
    rx, ry, bx, by = [0] * 4
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx,by = i,j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    init()
    while q :
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10 : break
        for i in range(4):
            next_rx, next_ry, count_r = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, count_b = move(bx, by, dx[i], dy[i])
            if board[next_bx][next_by] == 'O' : continue
            if board[next_rx][next_ry] == 'O' : print(depth); return
            if next_bx == next_rx and next_ry == next_by :
                if count_r > count_b:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else :
                    next_bx -= dx[i]
                    next_by -= dy[i]
            if not visited[next_rx][next_ry][next_bx][next_by]:
                q.append((next_rx, next_ry, next_bx, next_by, depth + 1))
                visited[next_rx][next_ry][next_bx][next_by] = True
    print(-1)

bfs()

