import sys
input = sys.stdin.readline

N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (1,-1,0,0), (0,0,1,-1) # 오른 왼  위  아래
visited = [[False] * M for _ in range(N)]
maxvalue_board = max(map(max, board))
maxvalue = 0

def dfs(x, y, count):
    global sum 
    global maxvalue
    print("----------", count, "---------")
    print("x is   ", x , " y is   ", y)
    if maxvalue > sum + maxvalue_board * (3-count) : return
    if count == 3 : maxvalue = max(maxvalue, sum); return
    for i in range(4):
        ni, nj = x + dx[i], y + dy[i]
        if  0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            if count == 1 :
                visited[ni][nj] = True
                sum += board[ni][nj]
                dfs(x,y,count+1)
                sum -= board[ni][nj]
                visited[ni][nj] = False
            sum += board[ni][nj]
            visited[ni][nj] = True
            dfs(ni, nj, count+1)
            sum -= board[ni][nj]
            visited[ni][nj] = False

# def ex(i, j):
#     global maxvalue
#     for k in range(4): 
#         tmp = board[i][j]
#         for m in range(3):
#             t = (k + m) % 4
#             ni = i + dx[t]
#             nj = j + dy[t]
#             if not (0<=ni<N and 0 <= nj < M): #하나라도 범위 밖이면
#                 break
#             tmp += board[ni][nj]
#         maxvalue = max(tmp, maxvalue)

for i in range(3,4):
    for j in range(3,4):
        sum = board[i][j]
        visited[i][j]= True
        dfs(i,j,0)
        visited[i][j] = False
        # ex(i,j)

print(maxvalue)
