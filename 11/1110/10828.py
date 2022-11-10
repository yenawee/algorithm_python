import sys
input = sys.stdin.readline

class Stack():
	def __init__(self):
		self.stack = []
	def push(self, data):
		self.stack.append(data)
	def pop(self):
		if self.isEmpty(): return -1
		else : return self.stack.pop()
	def isEmpty(self):
		if len(self.stack) == 0 : return 1
		else : return 0
	def size(self):
		print(len(self.stack))
	def top(self):
		if self.isEmpty(): print(-1)
		else : print(self.stack[-1])

N = int(input())

stack = Stack()
for _ in range(N):
	s = input().rstrip()
	if ' ' in s : cmd, n = s.split()
	else :
		cmd = s
	if cmd == 'push' : stack.push(n)
	elif cmd == 'pop' : print(stack.pop())
	elif cmd == 'top' : stack.top()
	elif cmd == 'size' : stack.size()
	elif cmd == 'empty' : print(stack.isEmpty())

