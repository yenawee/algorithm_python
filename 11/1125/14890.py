N, L = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

count = 0

def check(line):
    for i in range(1, N):
        if abs(line[i] - line[i-1]) > 1 : return False
        if line[i] > line[i-1]:
            for k in range(L):
                if i - 1 - k < 0 or slope[i-1-k] or line[i-1] != line[i-1-k]:
                    return False
            for k in range(L):
                slope[i-1-k] = True
        elif line[i] < line[i-1]:
            for k in range(L):
                if i + k >= N or slope[i+k] or line[i] != line[i+k]:
                    return False
            for k in range(L):
                slope[i+k] = True
    return True

for i in range(N):
    slope = [False] * N
    if (check([board[i][j] for j in range(N)])):
        count += 1

for j in range(N):
    slope = [False] * N
    if (check([board[i][j] for i in range(N)])):
        count += 1

print(count)
        