from collections import deque
import sys

router = deque()

N = int(input()) #deque size

while (True):
    packet = int(sys.stdin.readline())
    if packet == -1 : print("empty") if len(router) == 0 else print(' '.join(map(str, list(router)))); break
    if packet == 0 : router.popleft()
    elif len(router) < N : router.append(packet)



