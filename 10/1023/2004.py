def count_(n, j):
	cnt = 0
	while n :
		n //= j
		cnt += n
	return cnt

n,m = map(int, input().split())

print(min(count_(n, 5) - count_(n-m, 5) - count_(m, 5), count_(n, 2) - count_(n-m, 2) - count_(m, 2)))
