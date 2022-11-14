from collections import deque


N, M = map(int, input().split())

nbr = list(map(int, input().split()))

n = deque()
for i in range(1, N+1):
	n.append(i)

cnt = 0
idx = 0
while (True):
	if idx == M : print(cnt); break
	tmp1 = 0
	while (n[tmp1] != nbr[idx]):
		tmp1+=1
	tmp2 = len(n) - 1
	tmp22 = 0
	while (n[tmp2] != nbr[idx]):
		tmp2 -=1
		tmp22 += 1
	if tmp1 < tmp22 + 1 :
		cnt += tmp1
		while (n[0] != nbr[idx]):
			n.append(n.popleft())
		n.popleft()
	else :
		cnt += tmp22 + 1
		while (n[0] != nbr[idx]):
			n.appendleft(n.pop())
		n.popleft()
	idx += 1


