N, M = map(int, input().split())

S = {input() for _ in range(N)}

D = [0] * M
D = [1 for _ in range(M) if input() in S]

print(sum(D))



