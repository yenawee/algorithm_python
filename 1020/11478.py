S = input()
ret =[]
for i in range(len(S) + 1):
	for j in range(i+1, len(S) + 1):
		ret.append(S[i:j])


print(len(set(ret)))


