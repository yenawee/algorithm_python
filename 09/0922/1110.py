cycle = 0

N = int(input())
M = N

while True :
	a = M // 10
	b = M % 10
	c = (a + b) % 10
	M = b * 10 + c
	cycle += 1
	if (M == N) : break
print(cycle)
