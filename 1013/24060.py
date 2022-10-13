def merge_sort(l : list, s : int, e:int):
	if s < e :
		q = (s + e) // 2
		merge_sort(l, s, q)
		merge_sort(l, q + 1, e)
		merge(l, s, q, e)

def merge(l : list, s : int, q : int, e: int):
	i = s
	j = q + 1
	tmp = []
	while i <= q and j <= e :
		if l[i] <= l[j]:
			tmp.append(l[i])
			i += 1
		else :
			tmp.append(l[j])
			j += 1
	while i <= q :
		tmp.append(l[i])
		i+= 1
	while j <= e :
		tmp.append(l[j])
		j+= 1
	i = s
	k = 0
	global cnt
	while i <= e :
		l[i] = tmp[k]
		cnt += 1
		if cnt == K : print(tmp[k]); exit()
		i+=1
		k+=1


N , K = map(int, input().split())

n_list = list(map(int, input().split()))

cnt = 0
merge_sort(n_list, 0, len(n_list) - 1)
print(-1)


