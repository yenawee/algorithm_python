N , M = map(int, input().split())

hear = {input() for _ in range(N)}

see = {input() for _ in range(M)}

ret = list(hear & see)

ret.sort()

print(len(ret))
print('\n'.join(ret))
