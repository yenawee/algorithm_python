N = int(input())

for i in range(N):
	list_ = list(map(int, input().split()))
	cnt = 0
	avg = sum(list_[1:]) / (len(list_) - 1)
	for score in list_[1 :] :
		if score > avg : cnt += 1
	print(f"{cnt / (len(list_) - 1) * 100:.2f}%")


