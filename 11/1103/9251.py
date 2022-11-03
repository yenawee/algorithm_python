str1 = [0] + list(input())
str2 = [0] + list(input())

lcs = [[0] * len(str2) for _ in range(len(str1))]

for i in range(len(str1)):
	for j in range(len(str2)):
		if i == 0 or j == 0 :
			continue
		if str1[i] == str2[j]:
			lcs[i][j] = lcs[i-1][j-1] + 1
		else :
			lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(max(max(lcs)))
