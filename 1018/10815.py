N = int(input())

sg = list(map(int, input().split()))
sg.sort()

M = int(input())

card = list(map(int, input().split()))

def binary_search(target , li):
	start = 0
	end = len(li) - 1
	while start <= end :
		mid = (start+ end) // 2
		if li[mid] == target : return 1
		elif li[mid] < target : start = mid + 1
		else : end = mid - 1
	return 0

for c in card :
	print(binary_search(c, sg), end = ' ')


