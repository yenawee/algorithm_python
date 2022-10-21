m = int(input())

h =[]
w = []

for _ in range(3):
	i, j = map(int, input().split())
	if i == 3 or i == 4 : h.append(j)
	else : w.append(j)

max_sq = max(h) * max(w)

w.pop(max(w))


