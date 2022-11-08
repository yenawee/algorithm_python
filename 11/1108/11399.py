N = int(input())

time = list(map(int, input().split()))

time.sort()

sum_ = [time[0]] + [0] * (N-1)
for i in range(1, N):
	sum_[i] = sum_[i-1] + time[i]

print(sum(sum_))
