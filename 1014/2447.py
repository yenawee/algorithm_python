def make_star(n):
	if n == 3 :
		star[0] = ['*', '*', '*']
		star[1] = ['*', ' ', '*']
		star[2] = ['*', '*', '*']
		return
	make_star(n // 3)
	a = n // 3
	for i in range(3):
		for j in range(3):
			if i == 1 and j == 1: continue
			for k in range(a):
				star[a * i + k][a * j : a * (j+1)] = star[k][:a]


N = int(input())

star = [[' ' for i in range(N)] for i in range(N)]


make_star(N)
for s in star : print(*s, sep='')





