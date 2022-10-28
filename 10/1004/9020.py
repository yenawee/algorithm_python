import sys

list = [False, False] + [True for i in range(2, 10001)]
for i in range(2, int(10000 ** 0.5) + 1) :
	if list[i] == True :
		for j in range(i + i, 10001, i) :
			list[j] = False

T = int(sys.stdin.readline())
for i in range(T):
	n = int(sys.stdin.readline())
	a,b = n // 2, n // 2
	while True:
		if list[a] and list[b]:
			print(a,b)
			break
		else :
			a -= 1
			b+=1
