import sys

f = [0, 1, 1] + [0] * 38
def fib(n : int):
    for i in range(3, n+1) :
        f[i] = f[i - 1] + f[i -2]
    return f[i]

N = int(sys.stdin.readline().strip())
print(fib(N), N-2)
