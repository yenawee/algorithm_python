N,K = map(int, input().split())

coin = [int(input()) for _ in range(N)]

coin = coin[-1::-1]

cnt = 0
for don in coin :
	cnt += K // don
	K %= don

print(cnt)

