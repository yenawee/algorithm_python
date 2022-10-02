import math

N = int(input())
T = int(math.sqrt(N))

while N % 2 == 0:
	print(2)
	N //= 2
for i in range(3, T + 1):
	while N % i == 0 :
		print(i)
		N //= i
	else : i += 2
if N > 1 : print(N)



