N, M, x, y, cmd = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd_list = map(int, input().split())

dx, dy = (0,0,-1,1), (1,-1,0,0)  # 오른쪽 왼쪽 위쪽 아래쪽
cube = [0,0,0,0,0,0]

def turn(dir):
    a,b,c,d,e,f = cube[0], cube[1], cube[2], cube[3], cube[4], cube[5]
    if dir == 1 :
        cube[0], cube[1], cube[2], cube[3], cube[4], cube[5] = c, b, f ,a , e , d
    if dir == 2 :
        cube[0], cube[1], cube[2], cube[3], cube[4], cube[5] = d, b, a, f, e, c
    if dir == 3 :
        cube[0], cube[1], cube[2], cube[3], cube[4], cube[5] = b, f , c, d, a,e
    if dir == 4 :
        cube[0], cube[1], cube[2], cube[3], cube[4], cube[5] = e, a, c, d, f,b 

def move(x,y):
    if board[x][y] == 0 :
        board[x][y] = cube[0]
    else : 
        cube[0] = board[x][y]
        board[x][y] = 0


for i in cmd_list:
    m, n = x+dx[i-1], y+dy[i-1]
    if 0 <= m < N and 0 <= n < M :
        turn(i)
        x, y = x+dx[i-1], y+dy[i-1]
        move(x,y)
        print(cube[5])
