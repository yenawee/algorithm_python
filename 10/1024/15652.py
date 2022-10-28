N, M = map(int, input().split())

depth = 0
ans = []

def back(depth, start):
    if depth == M : print(' '.join(map(str, ans))); return
    for i in range(start, N + 1):
        ans.append(i)
        back(depth + 1, i)
        ans.pop()
back(0, 1) 