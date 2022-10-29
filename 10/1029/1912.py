N = int(input())
num = list(map(int, input().split()))

for i in range(1, N):
    num[i] = max(num[i - 1] + num[i], num[i])
print(max(num))
