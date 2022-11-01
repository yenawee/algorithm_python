N = int(input())

nbr = [0] + list(map(int, input().split()))

#dp = [0] * (N + 1)

#for i in range(1, N + 1):
#	dp[i] = 1
#	for j in range(i):
#		if nbr[j] < nbr[i]:
#			dp[i] = max(dp[i], dp[j] + 1)

#print(max(dp))

def binary_search(l, r, target):
	while l < r :
		mid = (l + r) // 2
		if li[mid] < target :
			l = mid + 1
		else : r = mid
	return r

li = [0] * (N + 1)
li[1] = nbr[1]
j = 1
for i in range(2, N + 1):
	if li[j] < nbr[i] : li[j + 1] = nbr[i]; j+=1
	else :
		idx = binary_search(1,j,nbr[i])
		li[idx] = nbr[i]

print(j)
