while (True):
    s = input()
    if (s == ".") : break
    s = list(s)
    check = []
    for p in s :
        if p == '(' or p == '[':
            check.append(p)
        if p == ')':
            if len(check) > 0 and check[-1] == '(':
                check.pop()
            else : check.append(p)
        if p == ']':
            if len(check) > 0 and check[-1] == '[':
                check.pop()
            else : check.append(p)
    if len(check) == 0 : print("yes")
    else : print("no")        

