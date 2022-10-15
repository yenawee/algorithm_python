from itertools import combinations

N , M = map(int, input().split())
card = [int(x) for x in input().split()]

#card.sort()

summ = 0
#L =[]
#for i in range(0, N - 2):
#	for j in range(i+1, N-1):
#		for k in range(j+1, N):
#			if card[i] + card[j] + card[k] > sum and card[i] + card[j] + card[k] <= M :
#				sum = card[i] + card[j] + card[k]

combi = combinations(card, 3)
for s in combi :
	if sum(s) > summ and sum(s) <= M :
		summ = sum(s)


print(summ)
