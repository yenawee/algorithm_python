def check(n : int):
	ret = 1
	for i in range(2, n):
		if n % i == 0 : ret = 0
	return ret


N = int(input())

number = list(map(int,input().split()))

cnt = 0
for nbr in number:
	if nbr == 1 : continue
	cnt += check(nbr)
print(cnt)
