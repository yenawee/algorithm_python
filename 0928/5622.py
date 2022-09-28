phone = {'ABC' : 3,'DEF': 4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}

str = input()

sum = 0
for i in phone.keys():
	for s in str:
		if s in i : sum += phone[i]

print(sum)







