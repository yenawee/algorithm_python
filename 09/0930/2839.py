N = int(input())

for y in range(N // 3 + 1):
	x = (N - 3 * y) // 5
	if 5 * x + 3 * y == N :
		print(x+y)
		break
else: print(-1)




# 5X + 3Y = N
# Y = (N - 5X) / 3

##while N >= 0 :
#	if N % 5 == 0 :
#		cnt+=(N//5)
#		print(cnt)
#		break
#	else :
#		N -= 3
#		cnt += 1
#else : print(-1)



