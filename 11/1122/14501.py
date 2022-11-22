N = int(input())

##브루트 포스
#s_list = [(0,0] + [list(map(int, input().split())) for _ in range(N)]
#ans = 0
#def sangdam(day, sum):
#	global ans
#	if day == N + 1 : # 상담날을 딱 맞췄다면
#		ans = max(ans, sum)
#		return ans
#	if day > N + 1 : # 날짜 범위 넘어가서 불가능
#		return
#	#상담을 한다
#	sangdam(day + s_list[day][0], sum + s_list[day][1])
#	#상담을 안한다
#	sangdam(day + 1, sum)

#sangdam(1,0)
#print(ans)

# 뒤부터 dp
#dp = []
#s_list = [list(map(int, input().split())) for _ in range(N)]
#for i in s_list :
#	dp.append(i[1])
#dp.append(0)

#for i in range(N-1, -1, -1):
#	if i + s_list[i][0] > N :
#		dp[i] = dp[i+1] # 상담 못함
#	else :
#		dp[i] = max(dp[i+1], dp[i+s_list[i][0]] + s_list[i][1]) #상담 안했을때랑 상담 했을 때의 맥스값

#print(dp[0])


dp = [0] * (N + 1)
s_list = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
	for j in range(i + s_list[i][0], N + 1):
		if dp[j] < dp[i] + s_list[i][1]:
			dp[j] = dp[i] + s_list[i][1]

print(dp[N])
