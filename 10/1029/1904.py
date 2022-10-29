fib = [0,1,2] + [0] * 1000000
n = int(input())
for i in range(3, n+1):
    fib[i] = (fib[i-1] + fib[i-2]) % 15746 


print(fib[n])

