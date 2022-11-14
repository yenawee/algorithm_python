from collections import deque

T = int(input())

for _ in range(T):
	command = str(input())
	N = int(input())
	l = input().lstrip('[').rstrip(']')
	if l : l = list(map(int, l.split(',')))
	q = deque()
	reverse = False
	for i in l : q.append(i)
	for cmd in command :
		if cmd == 'R' :
			if reverse : reverse = False
			else : reverse = True
		if cmd == 'D' :
			if len(q) == 0 : print("error"); break
			if reverse : q.pop()
			else : q.popleft()
	else :
		print('[', end='')
		if reverse : print(','.join(map(str, list(q)[-1::-1])), end='')
		else : print(','.join(map(str,list(q))), end ='')
		print(']')
