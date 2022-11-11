import sys

N = int(sys.stdin.readline())
l = [int(sys.stdin.readline().rstrip()) for _ in range(N)]


idx = 0
stack = []
i = 1
printlist = []
while (True):
    if idx == N : break
    if len(stack) > 0 and stack[-1] > l[idx]: 
        break 
    if len(stack) > 0 and stack[-1] == l[idx] : 
        stack.pop()
        printlist.append('-')
        idx += 1
    else:
        if i < N + 1:
            stack.append(i)
            printlist.append('+')
            i += 1

if len(stack) != 0 : print("NO")
else : print("\n".join(printlist))

