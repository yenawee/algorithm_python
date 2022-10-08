from collections import Counter

N = int(input())

l = [int(input()) for _ in range(N)]

print("%.f" %(sum(l)/N))
l.sort()
print(l[N//2])


c = Counter(l).most_common()

print(c[1][0]) if len(c) > 1 and c[0][1] == c[1][1] else print(c[0][0])


print(l[-1] - l[0])









