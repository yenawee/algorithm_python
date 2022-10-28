N = int(input())

for i in range(N):
	summ = sum(map(int, str(i)))
	if i + summ == N : print(i); exit()

print(0)
