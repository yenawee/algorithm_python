from collections import deque

N, K = map(int, input().split())
pp = deque()

for i in range(1, N+1):
    pp.append(i)

result = []

while (True):
    if len(pp) == 0 : print('<' + ', '.join(map(str,result)) + '>'); break
    for i in range(K - 1):
        pp.append(pp.popleft())
    result.append(pp.popleft())



