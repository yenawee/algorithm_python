import sys

N , M = map(int,input().split())

dic = {}
for i in range(1, N+1):
	str = input()
	dic[i] = str
	dic[str] = i

ret = []
for _ in range(M):
	i = sys.stdin.readline().strip()
	if i.isdigit() : ret.append(dic[int(i)])
	else : ret.append(dic[i])

print(*ret, sep='\n')












