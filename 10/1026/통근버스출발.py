import sys

N = int(sys.stdin.readline())

a = [0] + list(map(int, sys.stdin.readline().split()))
arr =[[0 for _ in range(N+1)] for _ in range(N+1)]

#  x => 1 ~ n 

for x in range(1, N+1):
    arr[x][N] = 0
    arr[x][N-1] = 1 if a[N] < x else 0
    for j in range(N-2, 0, -1):
        if a[j + 1] < x : 
            arr[x][j] = arr[x][j + 1] + 1
        else : 
            arr[x][j] = arr[x][j+1]

sum = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        if a[i] < a[j] :
            sum += arr[a[i]][j]

print(sum)
