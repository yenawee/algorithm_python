
point = [list(map(int,input().split())) for _ in range(3)]

if point[0][0] == point[1][0] : x = point[2][0]
elif point[0][0] == point[2][0] : x = point[1][0]
else : x = point[0][0]

if point[0][1] == point[1][1] : y = point[2][1]
elif point[0][1] == point[2][1] : y = point[1][1]
else : y = point[0][1]

print(x,y)

#x1, y1 = map(int, input().split())
#x2, y2 = map(int, input().split())
#x3, y3 = map(int, input().split())

#x4, y4 = x1^x2^x3, y1^y2^y3
#print(x4, y4)
