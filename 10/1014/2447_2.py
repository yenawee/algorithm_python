


def make_star(n):
	if n == 1 : return ['*']
	stars = make_star(n//3)
	L = []
	for s in stars : L.append(s * 3)
	for s in stars : L.append(s + ' ' * (n//3) + s)
	for s in stars : L.append(s * 3)
	return L

N = int(input())
stars = make_star(N)
for s in stars : print(*s, sep='')

