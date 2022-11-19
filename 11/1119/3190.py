from collections import deque

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
	a, b = map(int, input().split())
	board[a - 1][b - 1] = 2

L = int(input())
direction_info = dict()
for _ in range(L):
	x, c = input().split()
	direction_info[int(x)] = c

q = deque()
x, y = 0, 0
board[x][y] = 1
q.append((0,0))
cnt = 0
dx, dy = (1,0,-1,0), (0,1,0,-1)

direction = 1 #처음엔 오른쪽

# 오른쪽 담에 왼쪽  1 -> 2
# 왼쪽 다음에 왼쪽  3 -> 0
# 위쪽 담에 왼쪽    2 -> 3
# 아래쪽 담에 왼쪽  0 -> 1
# 왼쪽 담에 오른쪽  3 -> 2
# 왼쪽 담에 왼쪽


def turn(info) :
	global direction
	if info == 'L' :
		direction = (direction + 1) % 4
	else :
		direction = (direction - 1) % 4



while True :
	cnt += 1 #시간을 하나씩 늘려준다
	x += dx[direction]
	y += dy[direction]
	if x < 0 or x >= N or y < 0 or y >= N : break # 벽 범위 넘어가면 끝낸다
	if board[x][y] == 2 : # 사과 만나면
		board[x][y] = 1
		q.append((x,y))
		if cnt in direction_info:
			turn(direction_info[cnt])
	elif board[x][y] == 0 : # 비어있으면
		board[x][y] = 1
		tx, ty = q.popleft() #꼬리 정보 뱉기
		board[tx][ty] = 0
		q.append((x,y))
		if cnt in direction_info:
			turn(direction_info[cnt])
	else : break # 뱀 몸통 만나면 끝낸다

print(cnt)






