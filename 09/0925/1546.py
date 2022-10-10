N = int(input())

score = list(map(int, input().split()))
max_score = max(score)

print(sum(score) / (max_score * N) * 100)
