
N = int(input())
#L = [i for i in range(666,10000666) if '666' in str(i)]
#print(L[N-1])


nbr = 666
cnt = 0
while True :
	if '666' in str(nbr):
		cnt +=1
		if N == cnt : print(nbr); exit()
	nbr +=1

