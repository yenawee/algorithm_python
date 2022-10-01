# 0층 : 1 2 3 4 5 6 7 8 9 10 ....
# 1층 : 1 1+2 1+2+3 1+2+3+4 1+2+3+4+5 ....
# 2층 : 1 1+1+2 1+1+2+1+2+3 1+1+2+1+2+3+1+2+3+4 ....
# 3층 : 1 1+1+1+2 1+1+1+2+1+1+2+1+2+3

# (3,3) = (2,1) + (2,2) + (2,3)

#내풀이
dp = [[-1 for col in range(15)]for row in range(15)]

def cnt(k, n :int):
	if dp[k][n] != -1 : return dp[k][n]
	if k == 0 : return n
	sum = 0
	for i in range (1, n + 1):
		sum += cnt(k-1, i)
	dp[k][n] = sum
	return (sum)

T =  int(input())
for i in range(T):
	k = int(input())
	n = int(input())
	print(cnt(k,n))

#다른 코드
#T = int(input())

#for i in range(T):
#	k = int(input())
#	n = int(input())
#	floor = [n for n in range(1, n+1)]
#	#0 1 2 3 4 5 6 7
#	for s in range(k):
#		for index in range(1, n):
#			floor[index] += floor[index - 1]
#	print(floor[-1])



