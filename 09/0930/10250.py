T = int(input())
for i in range(T):
	H,W,N=map(int,input().split())
	door = N // H + 1
	floor = N % H
	if floor == 0 :
		floor = H
		door -= 1
	print(f"{floor}{door:02d}")
