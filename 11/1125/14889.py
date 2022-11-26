from itertools import combinations, permutations

N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]

c = list(combinations(range(N), N//2))

res = []
for l in c :
	sum = 0
	k = list(permutations(l, 2))
	for n in k :
		sum += power[n[0]][n[1]]
	res.append(sum)

min_ = 100

for i in range(len(res) // 2):
	min_= min(min_, abs(res[i]- res[-1-i]))
print(min_)
