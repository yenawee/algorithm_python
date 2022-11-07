N = int(input())

meeting = [list(map(int, input().split())) for _ in range(N)]

meeting.sort(key=lambda x: (x[1], x[0]))

last = 0
cnt = 0
for m in meeting :
	if last <= m[0]:
		cnt +=1
		last = m[1]

print(cnt)

