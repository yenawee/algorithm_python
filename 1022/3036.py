def get_gcd(a, b):
	while b : a, b = b, a%b
	return a


N = int(input())

ring = list(map(int, input().split()))

for i in range(1, len(ring)):
	gcd = get_gcd(ring[0], ring[i])
	print(ring[0] // gcd,'/',ring[i]//gcd, sep='')
