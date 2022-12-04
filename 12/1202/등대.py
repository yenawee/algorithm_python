def solution(n, lighthouse):
    dic = dict(zip([i for i in range(1, n+ 1)], [[] for _ in range(n)]))
    for l in lighthouse:
        dic[l[0]].append(l[1])
        dic[l[1]].append(l[0])
    
    answer = 0
    visited = [0] * (n + 1)

    def dfs(idx):
        visited[idx] = 1
        p, np = 1, 0
        for n in dic[idx]:
            if visited[n] : continue
            rp, rnp = dfs(n)
            p += min(rp, rnp)
            np += rp
        return p, np
    print(min(dfs(1)))
