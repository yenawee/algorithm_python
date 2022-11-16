def quadtree(x,y,N):
	global minus, zero, plus
	item = all[x][y]
	for i in range(x, x+N):
		for j in range(y, y+N):
			if all[i][j] != item:
				quadtree(x, y, N//3)
				quadtree(x + N//3, y, N//3)
				quadtree(x + 2 * N // 3, y, N//3)
				quadtree(x, y + N//3, N//3)
				quadtree(x + N//3, y + N// 3, N//3)
				quadtree(x + 2 * N//3, y + N // 3, N//3)
				quadtree(x, y + 2 * N // 3, N//3)
				quadtree(x + N // 3, y + 2 * N // 3, N//3)
				quadtree(x + 2 * N // 3, y + 2 * N // 3, N//3)
				return
	if item == -1 : minus +=1
	if item == 0 : zero += 1
	if item == 1 : plus += 1

minus = 0
zero = 0
plus = 0

N = int(input())
all = [list(map(int, input().split())) for _ in range(N)]
quadtree(0,0,N)
print(minus)
print(zero)
print(plus)

