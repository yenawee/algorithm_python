
#def find(start, end) :
#    global K
#    if start == end : return
#    mid = (start+end)//2
#    find(start, mid) ; find(mid+1, end)
#    if K <=end-start+1 :
#        J = sorted(I[start:end+1])
#        print(J[K-1]) ; exit()
#    K -= end-start+1

#N, K = map(int,input().split()) ; I = list(map(int,input().split()))
#find(0, N-1) ; print(-1)

def solve(n, k, nums):

    def solve_rec(beg, l):
        if l <= 1:
            return None
        half_len = (l + 1) // 2
        if (ret := solve_rec(beg, half_len)) is not None:
            return ret
        if (ret := solve_rec(beg + half_len, l - half_len)) is not None:
            return ret
        nonlocal k
        if k <= l:
            return sorted(nums[beg:beg + l])[k - 1]
        else:
            k -= l
            return None

    return solve_rec(0, n)


def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    answer = solve(N, K, A)
    print('-1' if answer is None else answer)
