dp = [1,1,1,2,2] + [0] * 100

for i in range(5, 101):
    dp[i] = dp[i - 1] + dp[i - 5]


T = int(input())

for _ in range(T):
    N = int(input())
    print(dp[N - 1])