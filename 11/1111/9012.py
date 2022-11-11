N = int(input())

for _ in range(N):
    check = []
    s = list(input())
    for p in s:
        if p == ')':
            if len(check) > 0 and check[-1] == '(':
                check.pop()
            else : check.append(p)
        if p == '(' :
            check.append(p)
    if len(check) == 0 : print("YES")
    else : print("NO")