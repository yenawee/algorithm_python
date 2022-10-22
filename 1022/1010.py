def combi(N, K):
	a = 1
	b = 1
	for i in range(K + 1, N + 1):
		a *= i
	for j in range(1, N - K + 1):
		b *= j
	return a//b
T = int(input())
for _ in range(T):
	N , M = map(int, input().split())
	print(combi(M,N))
