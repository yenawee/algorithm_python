l = input().upper()
list = []

for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
	list.append(l.count(ch))
print(chr(list.index(max(list)) + 65)) if list.count(max(list)) == 1  else print('?')
