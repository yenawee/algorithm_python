N = int(input())

coor = []
for _ in range(N) :
	coor.append(list(map(int, input().split())))

coor.sort(key = lambda x:(x[0],x[1]))
for i in range(N) : print(*coor[i])

