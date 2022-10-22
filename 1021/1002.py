T = int(input())

for _ in range(T):
	x1, x2, r1, y1, y2, r2 = map(int, input().split())

	if x1 == y1 and x2 == y2 and r1 == r2 :
		print(-1)
		continue
	distance = ((y1 - x1)**2 + (y2-x2)**2)**0.5
	if distance == r1 + r2 or distance == abs(r1-r2) : print(1)
	elif abs(r1-r2) < distance < r1+r2 : print(2)
	else : print(0)
