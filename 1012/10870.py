
#def fibonazzi(n: int):
#	if n == 0 : return 0
#	elif n == 1 : return 1
#	return fibonazzi(n-1) + fibonazzi(n-2)

#print(fibonazzi(int(input())))

a=0;b=1;n=1
exec("a,b=b,a+b;n+=1;"*int(input()))
print(a)
print(b)
print(n)

#0 1 1 2 3 5 8 13 ...
