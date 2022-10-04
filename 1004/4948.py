list = [False, False] + [True for i in range(2, 246913)]
for n in range(2, int((246913)**0.5) + 1):
	if list[n] == True :
		for j in range(n + n, 246913, n):
			list[j] = False


while True :
	k = int(input())
	if k == 0 : break
	print(sum(list[k+1:2*k+1]))




