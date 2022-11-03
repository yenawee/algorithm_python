N, K = map(int, input().split())
bag = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N+1)]
for i in range(1, N+1):
	for j in range(1, K + 1):
		# i를 넣을 수 있는 경우
		if j-bag[i][0] >= 0:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i][0]] + bag[i][1])
		# i를 넣지 못하는 경우
		else :
			dp[i][j] = dp[i-1][j]
print(dp)
