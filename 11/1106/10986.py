
N, M = map(int, input().split())
nbr = list(map(int, input().split()))
cnt = 0
remain = [1] + [0] * (M - 1)
sum = [0] * (N+1)

for i in range(1, N+1):
    sum[i] = (sum[i-1] + nbr[i-1]) % M
    remain[sum[i]] += 1
for i in remain:
    cnt += (i * (i-1)) // 2
print(cnt)