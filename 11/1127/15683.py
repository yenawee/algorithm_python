import copy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M) :
        if board[i][j] in [1,2,3,4,5] : cctv.append((board[i][j], i, j))      

dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
mode = [
    [],
    [[0], [1], [2], [3]],
    [[1,3], [0,2]],
    [[0,3], [0,1], [2, 3], [2, 1]],
    [[0,1,3], [0,1,2], [0,2,3], [1,2,3]],
    [[0,1,2,3]]
]

def fill(board, i, x, y):
    for l in i :
        nx = x
        ny = y
        while True:
            nx += dx[l]
            ny += dy[l]
            if nx < 0 or nx > N -1 or ny < 0 or ny > M-1 :
                break
            if board[nx][ny] == 6 : break
            if not board[nx][ny] : board[nx][ny] = 7


min_value = 1e9
def dfs(depth, board):
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range(N):
            count += board[i].count(0)
        min_value = min(min_value, count)
        return
    temp = copy.deepcopy(board)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(board)
    
dfs(0, board)
print(min_value)