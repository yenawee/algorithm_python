from collections import deque # rotate 는 deque 로 구현
gears = {} # dictionary로 받았다
for i in range(1, 5):
    gears[i] = deque(list(map(int, input())))
K = int(input())

def check_right(num, dirs):
    if num > 4 or gears[num - 1][2] == gears[num][6]: return
    check_right(num+1, -dirs)
    gears[num].rotate(dirs)

def check_left(num, dirs):
    if num < 1 or gears[num][2] == gears[num+1][6]:return
    check_left(num-1, -dirs)
    gears[num].rotate(dirs)

for _ in range(K):
    num, dirs = map(int, input().split())
    #왼쪽 오른쪽 회전
    check_right(num + 1, -dirs)
    check_left(num -1 , -dirs)
    gears[num].rotate(dirs)

sum = 0
for i in range(1, 5):
    sum += (2**(i-1)) * gears[i][0]
print(sum)