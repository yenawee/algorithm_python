s= input()
for i in 'abcdefghizklmnopqrstuvwxyz' :
	if i in s : print(s.index(i), end=' ')
	else : print(-1, end = ' ')
