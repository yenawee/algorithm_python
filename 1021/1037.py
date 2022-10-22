N = int(input())

if N == 1 : print(int(input()) ** 2); exit()

y = list(map(int, input().split()))


y.sort()

print(y[0]*y[-1])



