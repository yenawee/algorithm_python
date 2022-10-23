T = int(input())
for _ in range(T):
	N = int(input())
	cloth = {}
	for _ in range(N) :
		i,j = input().split()
		if j in cloth : cloth[j] += 1
		else : cloth[j] = 1
	cnt = 1
	for i in cloth:
		cnt *= (cloth[i] + 1)
	print(cnt - 1)
