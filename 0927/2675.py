n = int(input())

for i in range(n):
	N, line = input().split()
	for ch in line :
		print(ch * int(N), end='')
	print()

