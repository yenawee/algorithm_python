N = int(input())

sang = list(map(int, input().split()))

dic = {}
for i in sang:
	if i not in dic :
		dic.setdefault(i, 1)
	else : dic[i] += 1

M = int(input())

nbr = list(map(int, input().split()))

for i in nbr:
	try : print(dic[i], end=' ')
	except : print(0, end=' ')


