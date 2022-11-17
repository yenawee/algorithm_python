import heapq, sys

heap = []

N = int(input())
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0 :
        if len(heap) == 0 : print('0')
        else : print(heapq.heappop(heap)[1])
    else : heapq.heappush(heap, (-n, n))