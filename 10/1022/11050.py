def combi(N, K):
	if comb[N][K] : return comb[N][K]
	a = 1
	b = 1
	for i in range(K + 1, N + 1):
		a *= i
	for j in range(1, N - K + 1):
		b *= j
	comb[N][K] = (a//b)
	return a//b

N, K = map(int, input().split())

comb = [[0 for i in range(1001)] for _ in range(1001)]

if comb[N][K] : print(comb[N][K] % 10007)
else : print(combi(N,K) % 10007)

# N! / K ! (N - K)!
# K + 1 ~ N / 1 ~ N - K
