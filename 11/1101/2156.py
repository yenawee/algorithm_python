N = int(input())

wine = [0] + [int(input()) for _ in range(N)]

dp = [[0]* 2 for _ in range(10001)]

sum =[0] * 10001

#dp[1][0] = wine[1]
#dp[1][1] = wine[1]
#if N >= 2 :
#	dp[2][0] = wine[1] + wine[2]
#	dp[2][1] = wine[2]
#if N >= 3:
#	dp[3][0] = wine[2] + wine[3]
#	dp[3][1] = wine[1] + wine[3]
#for i in range(4):
#	sum[i] = max(dp[i][0], dp[i][1])
#for i in range(4, N + 1) :
#	dp[i][0] = max(dp[i-1][1], dp[i-4][0]  + wine[i-1]) + wine[i]
#	dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + wine[i]
#	sum[i] = max(dp[i][0], dp[i][1])
#print(max(sum))

for i in range(3, N+1):
	dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

