import sys
input= sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
# op_n = list(map(int, input().split()))
# op = ['+'] * op_n[0] + ['-'] * op_n[1] + ['*'] * op_n[2] + ['/'] * op_n[3]
add, minus, multiple, divide = map(int, input().split())
visited = [0] * (N - 1)
Min = 1e9
Max = -1e9


def back(depth, num, add, minus, multiple, divide):
    global Min, Max
    if depth == N:
        Max = max(num, Max)
        Min = min(num, Min)
    if add > 0 : back(depth + 1, num + nums[depth], add - 1, minus, multiple, divide)
    if minus > 0 : back(depth + 1, num - nums[depth], add, minus - 1, multiple, divide)
    if multiple > 0 : back(depth + 1, num * nums[depth], add, minus, multiple - 1, divide)
    if divide > 0 : back(depth + 1, int(num / nums[depth]), add, minus, multiple, divide - 1)

back(1, nums[0], add, minus, multiple,divide)

# def back(tmp, depth):
#     global Min, Max
#     if depth == N - 1 :
#         Max = max(tmp, Max)
#         Min = min(tmp, Min)
#         return
#     for i in range(N - 1): 
#         tmp_ = tmp
#         if visited[i] == 0 :
#             if op[i] == '+':
#                 tmp += nums[depth+1]
#             elif op[i] == '-':
#                 tmp -= nums[depth+1]
#             elif op[i] == '*':
#                 tmp *= nums[depth+1]
#             elif op[i] == '/':
#                 tmp = int(tmp/ nums[depth+1]) 
#             visited[i] = 1
#             back(tmp, depth+1)
#             tmp = tmp_
#             visited[i] = 0
# back(nums[0], 0)
print(Max)
print(Min)
