
import math
N = int(input())

f = list(str(math.factorial(N)))

cnt = 0
while f[-1] == '0':
	cnt+=1
	f=f[:-1]
print(cnt)




