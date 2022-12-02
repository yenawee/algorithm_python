from itertools import combinations

N , M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []

for i in range(N):
	for j in range(N):
		if board[i][j] == 1 : home.append([i,j])
		elif board[i][j] == 2 : chicken.append([i,j])


chicken_M = list(combinations(chicken, M))

dis = 50000

for k in chicken_M :
	dis_ = 0
	for h in home :
		min_ = 150
		for j in k :
			tmp = abs(h[0] - j[0]) + abs(h[1] - j[1])
			min_ = min(min_, tmp)
		dis_ += min_
	dis = min(dis, dis_)

print(dis)

