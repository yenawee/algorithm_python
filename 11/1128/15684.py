import sys
input = sys.stdin.readline

N, M , H = map(int, input().split())
visited = [[False] * (N+1) for _ in range(H+1)]
combi = []

for _ in range(M):
    i, j = map(int, input().split())
    visited[i][j] = True

for i in range(1, H+1):
    for j in range(1, N):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            combi.append([i,j])

def check():
    for i in range(1, N+1):
        now = i
        for j in range(1, H+1):
            if visited[j][now - 1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i : return False
    return True    

def dfs(depth, index):
    global answer
    if depth >= answer : return
    if check() : answer = depth; return
    for c in range(index, len(combi)):
        x, y = combi[c]
        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(depth + 1, c + 1)
            visited[x][y] = False

answer = 4
dfs(0,0)
print(answer if answer < 4 else -1)


