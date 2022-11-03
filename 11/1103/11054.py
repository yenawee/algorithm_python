N = int(input())
k = list(map(int,input().split()))
nbr = [0] + k
dp_increase = [0,1] + [1]*N
dp_decrease = [0,1] + [1]*N
nbr_rev = [0] + k[::-1]
for i in range(1, N + 1):
	for j in range(1, i + 1):
		if nbr[j] < nbr[i]:
			dp_increase[i] = max(dp_increase[i], dp_increase[j]+1)
		if nbr_rev[j] < nbr_rev[i]:
			dp_decrease[i] = max(dp_decrease[i], dp_decrease[j]+1)
result = [0] * (N+1)
for i in range(1,N+1):
	result[i] = dp_increase[i] + dp_decrease[N -i + 1] - 1
print(max(result))

