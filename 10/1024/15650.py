N, M = map(int, input().split())

depth = 0
visited = [0] * (N + 1)
ans = []

def back(depth, s, e):
    if depth == M : print(' '.join(map(str, ans))); return
    for i in range(s, e + 1):
        if not visited[i] :
            ans.append(i)
            visited[i] = 1
            back(depth + 1, i + 1, e)
            visited[i] = 0
            ans.pop()
back(0, 1, N) 