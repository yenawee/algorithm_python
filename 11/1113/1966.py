from collections import deque

T = int(input())

for _ in range(T):
	N , M = map(int, input().split())
	priority = list(map(int, input().split()))
	priority_queue = deque()
	idx_queue = deque()
	result = []
	for i in range(N):
		priority_queue.append(priority[i])
		idx_queue.append(i)
	while (True):
		if len(priority_queue) == 0 : break
		while (priority_queue[0]!= max(priority_queue)):
			priority_queue.append(priority_queue.popleft())
			idx_queue.append(idx_queue.popleft())
		priority_queue.popleft()
		result.append(idx_queue.popleft())
	print(result.index(M) + 1)
