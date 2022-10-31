N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
sum = [[0] * 2 for _ in range(N+1)]

sum[1][1] = stairs[1]
sum[1][0] = stairs[1]
for i in range(2, N + 1):
	sum[i][0] = sum[i - 1][1] + stairs[i]
	sum[i][1] = max(sum[i - 2][0], sum[i-2][1]) + stairs[i]

print(max(sum[N][0], sum[N][1]))
