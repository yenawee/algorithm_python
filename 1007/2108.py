N = int(input())

l = [int(input()) for _ in range(N)]

print(int(sum(N) / N))
l.sort()
print(l[N//2])

c = []
for i in range(N) :
	c[i] = list.count(list[i])
if c.count(max(c)) >= 2 :


