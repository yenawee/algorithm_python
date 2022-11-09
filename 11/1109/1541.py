eq = input().split('-')
sum = 0
for i in eq[0].split('+'):
	sum += int(i)
for i in eq[1:] :
	for j in i.split('+'):
		sum -= int(j)
print(sum)
