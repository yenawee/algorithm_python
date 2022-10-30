N = int(input())
tri = [list(map(int, input().split())) for  _ in range(N)]

dp = [[] for _ in range(N)]

dp[0] = tri[0]

for i in range(1, N) :
    dp[i] = [0] * (i + 1)
    dp[i][0] = tri[i][0] + dp[i-1][0]
    dp[i][-1] = tri[i][-1] + dp[i-1][-1]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[-1]))

