N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

cnt = []
for i in range(N):
	count = 1
	for j in range(N):
		if table[i][0] < table[j][0] and table[i][1] < table[j][1] : count+=1
	cnt.append(count)

print(*cnt)

