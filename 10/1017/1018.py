def white(l : list):
	cnt = 0
	for i in range(8) :
		if i % 2 == 0 and l[i] != 'W' : cnt+=1
		elif i % 2 == 1 and l[i] != 'B' : cnt +=1
	return cnt

def black(l : list):
	cnt = 0
	for i in range(8) :
		if i % 2 == 0 and l[i] != 'B' : cnt+=1
		elif i % 2 == 1 and l[i] != 'W' : cnt +=1
	return cnt


N,M = map(int, input().split())

big_chess = [list(input()) for _ in range(N)]


# i <= N - 8 , j <= M - 8
cnt = []
for i in range(N - 7):
	for j in range(M - 7):
		if_white = 0
		if_black = 0
		k = i
		for b in range(4):
			if_white += white(big_chess[k][j:j+8])
			if_black += black(big_chess[k][j:j+8])
			if_white += black(big_chess[k+1][j:j+8])
			if_black += white(big_chess[k+1][j:j+8])
			k += 2
		c = if_white if if_white < if_black else if_black
		cnt.append(c)
print(min(cnt))







