T = int(input())

def is_in_circle(circle : list, x: int, y: int):
	distance = ((x - circle[0])**2 + (y - circle[1])**2)**0.5
	if distance < circle[2] : return True
	return False

for _ in range(T):
	x1, y1, x2, y2 = map(int, input().split())
	N = int(input())
	circles = [list(map(int, input().split())) for _ in range(N)]
	cnt1 = 0
	cnt2 = 0
	cnt3 = 0
	for circle in circles :
		cnt1 += is_in_circle(circle, x1, y1)
		cnt2 += is_in_circle(circle, x2, y2)
		cnt3 += (is_in_circle(circle,x1, y1) and is_in_circle(circle, x2, y2))
	print(0) if cnt1 == cnt2 == cnt3 else print(cnt1+cnt2-2*cnt3)



