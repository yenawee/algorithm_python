
def quadtree(x,y,N):
	item = all[x][y]
	for i in range(x,x+N):
		for j in range(y,y+N):
			if item != all[i][j]:
				print('(',end='')
				quadtree(x, y, N//2)
				quadtree(x, y + N//2, N//2)
				quadtree(x + N//2, y, N//2)
				quadtree(x+N//2, y+N//2, N//2)
				print(')',end='')
				return
	print(item, end='')


N = int(input())
all = [list(map(int, input())) for _ in range(N)]
quadtree(0,0,N)

