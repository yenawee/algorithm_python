import sys

N, B = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

a.sort()

cost = 0
for i in range(len(a) - 1) :
	while a[i] < a[i+1]:
		l, r = a[i], a[i+1]
		while cost + (r-l) ** 2 >= B :
			r -= 1
			if r-l == 0 : print(a[0]); exit()
		a[i] = r
		cost += (r-l) ** 2
print(a)












