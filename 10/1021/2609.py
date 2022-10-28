a,b = map(int, input().split())

max_y = 1
for i in range(2, min(a,b) + 1):
	if a % i == 0 and b % i == 0 : max_y = i

print(max_y, max(a,b) * (min(a,b) // max_y ))
