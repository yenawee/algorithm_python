import sys
from collections import deque

class que():
	def __init__(self):
		self.queue = deque()
	def isEmpty(self):
		if len(self.queue) == 0 : return 1
		return 0
	def push(self, data):
		self.queue.append(data)
	def pop(self):
		if (self.isEmpty()):
			return -1
		return (self.queue.popleft())
	def front(self):
		if (self.isEmpty()) : return -1
		return self.queue[0]
	def back(self):
		if (self.isEmpty()) : return -1
		return self.queue[-1]
	def size(self):
		return (len(self.queue))

N = int(input())

q = que()
for _ in range(N):
	s = sys.stdin.readline().rstrip()
	if ' ' in s :
		cmd, n = s.split()
		n = int(n)
	else : cmd = s
	if cmd == 'push' : q.push(n)
	elif cmd == 'pop' : print(q.pop())
	elif cmd == 'size' : print(q.size())
	elif cmd == 'empty' : print(q.isEmpty())
	elif cmd == 'front' : print(q.front())
	elif cmd == 'back' : print(q.back())
