N = int(input())

list = [int(input()) for _ in range(N)]

for k in range(N-1, 0, -1) :
	for i in range(k) :
		if list[i] > list[i+1]:
			list[i], list[i+1] = list[i+1], list[i]
print(list)
