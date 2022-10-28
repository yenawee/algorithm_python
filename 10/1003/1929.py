#import math

#def check_sosu(n : int):
#	if n % 2 == 0 : return False
#	else :
#		for i in range(3, int(math.sqrt(n)) + 1):
#			if n % i == 0 : return False
#			else : i += 2
#	return True


#M, N = map(int, input().split())

#for i in range(M, N + 1):
#	if i == 1 : continue
#	elif i == 2 :print(2)
#	elif check_sosu(i) : print(i)

M, N = map(int, input().split())

list = [True for i in range(0, N+1)]

for i in range(2,int(N ** 0.5) + 1):
	if (list[i] == True) :
		for j in range(i+i, N + 1, i) :
			list[j] = False
for k in range(M, N+1):
	if k == 1 : continue
	elif list[k] : print(k)
