t = int(input())

graph = [[0] * 101 for _ in range(101)]

dx, dy = (1,0,-1,0), (0, -1, 0, 1)

for _ in range(t):
	x,y,d,g = map(int, input().split())
	graph[y][x] = 1
	#curve list 만들기
	curve = [d]
	for i in range(g):
		for j in range(len(curve)-1, -1, -1):
			curve.append((curve[j] + 1) % 4)
	#드래콘 커브 만들기
	for i in range(len(curve)):
		x += dx[curve[i]]
		y += dy[curve[i]]
		if x < 0 or x >= 101 or y < 0 or y >= 101 :
			continue
		graph[x][y] = 1

answer = 0
for i in range(100):
	for j in range(100):
		if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
			answer += 1

print(answer)
