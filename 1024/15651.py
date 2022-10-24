N, M = map(int, input().split())

depth = 0
ans = []

def back(depth, N):
    if depth == M : print(' '.join(map(str, ans))); return

    for i in range(1, N + 1):
            ans.append(i)
            back(depth + 1, N)
            ans.pop()

back(0, N) 