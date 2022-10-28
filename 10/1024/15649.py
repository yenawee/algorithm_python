N, M = map(int, input().split())

depth = 0
visited = [0] * (N + 1)
ans = []

def back(depth, N):
    if depth == M : print(' '.join(map(str, ans))); return

    for i in range(1, N + 1):
        if not visited[i] :
            ans.append(i)
            visited[i] = 1
            back(depth + 1, N)
            visited[i] = 0
            ans.pop()

back(0, N) 

