def self_num(n: int):
	result = n
	while n > 0:
		result += n%10
		n = n//10
	return result

list_ = [True for i in range(1, 10100)]

for i in range(1, 10001):
	list_[self_num(i)] = False

for k in range(1,10001):
	if list_[k] : print(k)



