N, K = map(int, input().split())
temp = list(map(int, input().split()))
sum = [0]
s = 0
for i in range(N):
	s+=temp[i]
	sum.append(s)
max = -1e7
i = 0
for j in range(K, N+1):
	c = sum[j] - sum[i]
	i+=1
	if c > max : max = c
print(max)
