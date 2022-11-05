import sys
input = sys.stdin.readline
str = input().rstrip()
N = int(input())
#l = []
#for c in 'abcdefghijklmnopqrstuvwxyz':
#	sum = [0] * (len(str)+1)
#	for i in range(1, len(str)+1):
#		if str[i-1] == c :
#			sum[i] = sum[i-1] + 1
#		else : sum[i] = sum[i-1]
#	l.append(sum)
l = [0] * 26
all = []
for c in str:
	l[ord(c) - 97] += 1
	all.append(l[:])

for _ in range(N):
	c, i, j = list(input().split())
	i,j = map(int, [i,j])
	if i :
		print(all[j][ord(c) - 97] - all[i-1][ord(c)-97])
	else : print(all[j][ord(c) - 97])
