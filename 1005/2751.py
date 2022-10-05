import sys

N = int(input())
list = [int(sys.stdin.readline()) for _ in range(N)]

print(*sorted(list))
