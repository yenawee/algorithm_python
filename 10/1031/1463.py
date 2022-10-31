N = int(input())
dp = [0] * 1000001

#  dp[i] = i 까지 계산했을 때 연산의 최소값

for i in range(2, N + 1):
    if i % 6 == 0 : dp[i] = min(dp[i - 1], dp[ i //3], dp[i//2]) + 1
    elif i % 3 == 0 : dp[i] = min(dp[i - 1], dp[ i // 3]) + 1
    elif i % 2 == 0 : dp[i] = min(dp[i - 1], dp[ i // 2]) + 1
    else : dp[i] = dp[i - 1] + 1

print(dp[N])