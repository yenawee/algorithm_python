x,y,w,h = map(int, input().split())

# (0,0)(w,0)(0,h)(w,h)

print(min(x,y,w-x, h-y))
