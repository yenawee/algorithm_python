N = int(input())

cnt = 0
for i in range(N):
	str = input()
	flag = True
	for x in range(len(str) - 1):
		if str[x] == str[x+1] : pass
		elif str[x] in str[x+1:] :
			flag = False
			break
	if (flag) : cnt += 1
print(cnt)

