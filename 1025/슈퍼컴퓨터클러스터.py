import sys

N, B = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
sum = 0

def get_sum(e):
    sum = 0
    for i in range(N):
        diff = e-a[i] if e-a[i]>0 else 0
        sum += diff**2
        if sum > B : break
    return sum

def binary_search(left, right):
    if left > right : return right
    mid = (left + right) // 2
    if get_sum(mid) == B : return mid
    elif get_sum(mid) > B :
        return (binary_search(left, mid - 1))
    else : return (binary_search(mid+1, right))
    
print(binary_search(0, 2000000000))