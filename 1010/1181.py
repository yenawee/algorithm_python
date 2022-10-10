N = int(input())

word = {input() for _ in range(N)}
word = list(word)

word.sort(key=lambda x : (len(x), x))

print('\n'.join(word))
