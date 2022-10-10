N = int(input())


a = 1
d = 6
layer = 1
if N == 1: print(1)
else :
	while not a < N <= a + d:
		layer +=1
		a += d
		d +=6
	print(layer + 1)



