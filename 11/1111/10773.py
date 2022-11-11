class Stack():
    def __init__(self) :
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) == 0 : 
            return 
        self.stack.pop()
    



stack = Stack()
K = int(input())

for _ in range(K):
    n = int(input())
    if n == 0 : stack.pop()
    else : stack.push(n)

print(sum(stack.stack))

