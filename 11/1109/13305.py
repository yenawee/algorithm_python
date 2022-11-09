N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

#cost_sum = cost[0] * distance[0]
min = cost[0]
#dist = 0
#for i in range(1, len(distance)):
#	if cost[i] < now :
#		cost_sum += now * dist
#		now = cost[i]
#		dist = distance[i]
#	else :
#		dist += distance[i]

#print(cost_sum + now * dist)
cost_sum = 0
for i in range(N-1):
	if min > cost[i] : min = cost[i]
	cost_sum += min * distance[i]
print(cost_sum)





