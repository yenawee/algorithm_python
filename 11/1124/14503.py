N, M = map(int, input().split())
r,c,d = map(int, input().split())

dx ,dy = (-1,0, 1, 0), (0,1,0,-1)


board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
visited[r][c] = True
count = 1

while True:
	flag = 0 # 청소 안함
	for  _ in range(4): #4방향 돌기
		d = (d + 3) % 4
		nr = r + dx[d]
		nc = c + dy[d]
		if 0<=nr<N and 0<= nc < M and board[nr][nc] == 0:
			if visited[nr][nc] == False:
				r= nr
				c = nc
				flag = 1 # 청소함
				visited[nr][nc] = True
				count += 1
				break
	# 다 돌려도 청소를 못했을 때
	if flag == 0 :
		#후진도 못하면
		if board[r - dx[d]][c - dy[d]] == 1:
			print(count)
			break
		else :
			r,c = r - dx[d],c - dy[d]




