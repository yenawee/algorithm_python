from collections import Counter
import sys
N = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(N)]
print(round(sum(l)/N))
l.sort()
print(l[N//2])
c = Counter(l).most_common(2)
if len(c) == 1 : print(c[0][0])
else :
	if c[0][1] == c[1][1] : print(c[1][0])
	else : print(c[0][0])
print(l[-1] - l[0])









