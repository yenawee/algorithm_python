def get_gcd(a, b):
	while (b) : a,b = b, a%b
	return a


T = int(input())

for _ in range(T):
	a,b = map(int, input().split())
	gcd = get_gcd(max(a,b), min(a,b))
	print(max(a,b) * (min(a,b) // gcd))
