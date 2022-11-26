N = int(input())

number = list(map(int, input().split()))

n = list(map(int, input().split()))

op = ['+'] * n[0] + ['-'] * n[1] + ['x'] * n[2] + ['/'] * n[3]

max_ = -1000000000
min_ = 1000000000


def f(i, res, plus, minus, mult, div):
	global max_, min_
	if plus == minus == mult == div == 0:
		max_ = max(max_, res)
		min_ = min(min_, res)
		return
	if plus > 0 :
		f(i+1, res + number[i], plus - 1, minus, mult, div)
	if minus > 0:
		f(i+1, res - number[i], plus, minus - 1, mult, div)
	if mult > 0:
		f(i+1, res * number[i], plus, minus, mult - 1, div)
	if div > 0:
		f(i+1, int(res / number[i]), plus, minus, mult, div-1)

f(1, number[0], n[0], n[1], n[2], n[3])
print(max_)
print(min_)
