l = []

def hanoi(n : int, from_pos : int,  to_pos:int, aux_pos :int):
	global cnt
	if n == 1 :
		cnt += 1
		l.append([from_pos, to_pos]); return
	hanoi(n-1, from_pos, aux_pos, to_pos)
	cnt += 1
	l.append([from_pos, to_pos])
	hanoi(n-1, aux_pos, to_pos, from_pos)


N = int(input())
cnt = 0

hanoi(N, 1,3,2)
print(cnt)
for i in l : print(*i)
