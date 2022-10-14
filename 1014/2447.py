def make_star(n : int):

	if n == 3 :
		ret = ['***', '* *', '***']
	if n == 9 :
		ret = ['***' * 3 + '* *' * 3 + '***' * 3,  ]
		n //= 3

	# print(n // 3) * 3
	# print(n // 3) + n // 3 * n//3 공백 + print(n // 3)
	# print(n // 3) * 3





N = int(input())


