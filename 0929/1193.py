N = int(input())

i = 1
while (i + 1) * i / 2 < N : i+=1

k = int(i * (i + 1) / 2) - N + 1

if i % 2:
	print(f'{k}/{i + 1 - k}')
else :
	print(f'{i + 1 -k}/{k}')

