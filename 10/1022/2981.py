def get_gcd(a, b):
	while b : a, b = b, a%b
	return a

N = int(input())

nbr = [int(input()) for _ in range(N)]
nbr.sort()
new_nbr = []
for i in range(1, len(nbr)):
	new_nbr.append(nbr[i] - nbr[i - 1])
gcd = new_nbr[0]
for i in range(1, len(new_nbr)) :
	gcd = get_gcd(gcd, new_nbr[i])

ret = []
for i in range(2, int(gcd**0.5)+ 1):
	if gcd % i == 0:
		ret.append(i)
		ret.append(gcd // i)
ret.append(gcd)

ret2 = list(set(ret))
ret2.sort()


print(*ret2)





