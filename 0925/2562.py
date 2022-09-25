list = []

for i in range(0,9):
	list.append(int(input()))

print(max(list))
print(list.index(max(list)) + 1)


