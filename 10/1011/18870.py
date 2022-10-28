N = int(input())

num = list(map(int, input().split()))
set_num = list(set(num))

set_num.sort()

ret = {}
n = 0
for i in set_num :
	ret[i] = n
	n += 1

for i in num : print(ret[i], end = ' ')
