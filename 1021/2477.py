m = int(input())

l = []
for _ in range(6):
	i,j = map(int, input().split())
	l.append(j)

i = 0
max1 = 0
max2 = 0
for n in l :
	if i % 2 == 0 :
		if n > max1 : max1=n; max1_ix = i
	elif i % 2 != 0:
		if n > max2 : max2=n; max2_ix = i
	i += 1

small1 = abs(l[(max1_ix + 1) % 6] - l[max1_ix - 1])
small2 = abs(l[(max2_ix + 1) % 6] - l[max2_ix - 1])

print((max1 * max2 - small1 * small2) * m)

