N = int(input())
line = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]
line.sort(key=lambda x:x[0])

def binary_search(l,r,target):
	while l < r:
		mid = (l+r)//2
		if lis[mid] < target:
			l = mid+1
		else : r = mid
	return r

nbr = [0] * (N+1)
for i in range(1, N+1):
	nbr[i] = line[i][1]

lis = [0] * (N + 1)
lis[1] = nbr[1]
j = 1
for i in range(2, N+1):
	if lis[j] < nbr[i] : lis[j + 1] = nbr[i]; j += 1
	else:
		idx = binary_search(1, j, nbr[i])
		lis[idx] = nbr[i]

print(N - j)


