N = int(input())

l = [list(input().split()) for _ in range(N)]

l.sort(key=lambda x:int(x[0]))

for i in range(N) : print(*l[i])
