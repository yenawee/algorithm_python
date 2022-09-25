N = int(input())

for i in range(N):
	list = input()
	score = 0
	sum = 0
	for i in list:
		if i == 'O' :
			score += 1
			sum += score
		else :
			score = 0
	print(sum)




