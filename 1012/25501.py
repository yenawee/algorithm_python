def recursion(str, l, r):
	global re
	re += 1
	if l >= r : return 1
	if str[l] != str[r] : return 0
	return recursion(str, l + 1, r - 1)


def is_palindrome(str):
	return (recursion(str, 0, len(str) - 1))



for _ in range(int(input())):
	re = 0
	str = input()
	print(is_palindrome(str), re)
