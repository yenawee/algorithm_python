from collections import deque

N = int(input())

card = deque()

for i in range(1, N+1):
    card.append(i)

while (True):
    if len(card) == 1 : print(card[0]) ; break
    card.popleft()
    card.append(card.popleft())



