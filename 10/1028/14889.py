def get_power(l):
	sum = 0 
	for i in l :
		for j in l : sum += S[i][j]
	return sum

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * 20
arr = [0] * (N // 2)
res = []

def back(s, depth):
	if depth == N // 2 :
		sum = get_power(arr)
		res.append(sum)
		return
	for i in range(s, N):
		if visited[i] == 0:
			arr[depth] = i
			visited[i] = 1
			back(i+1, depth+1)
			visited[i] = 0

back(0,0)
minn = 300
l = len(res)
for i in range(l // 2):
	num = abs(res[i] - res[l - i - 1])
	if num < minn : minn = num
print(minn)