import sys

input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

sum = [[0] * (N + 1)  for _ in range(N + 1)]

for i in range(1,N+1):
    for j in range(1, N+1):
        sum[i][j] = sum[i][j-1] + table[i-1][j-1]
for i in range(1,N + 1):
    for j in range(2, N + 1):
        sum[j][i] = sum[j-1][i] + sum[j][i] 
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1])
    