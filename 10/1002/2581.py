def check(n : int):
	ret = 1
	for i in range(2, n):
		if n % i == 0 :
			ret = 0
			break
	return ret


M = int(input())
N = int(input())

list = []
for n in range(M, N+1):
	if n == 1 : continue
	if check(n) : list.append(n)
print(-1) if len(list)== 0 else print(sum(list), min(list), sep='\n')
