while True:
	p = list(map(int, input().split()))
	if p == [0,0,0] : break
	p.sort()
	if p[2] ** 2 == p[0] ** 2 + p[1] ** 2 : print('right')
	else : print('wrong')
