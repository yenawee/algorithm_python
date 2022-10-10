N = int(input())

coor = [list(map(int, input().split())) for _ in range(N)]

coor.sort()

for i in coor : print(i[0], i[1])
