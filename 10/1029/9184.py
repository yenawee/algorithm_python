w_arr = [[[1] * 21 for _ in range(21)] for _ in range(21)]

# def w(a,b,c):
#     if a == 0  or b == 0 or c == 0 : return 1
#     if w_arr[a][b][c] : return w_arr[a][b][c]
#     if a < b and b < c : 
#         tmp = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#         w_arr[a][b][c] = tmp
#         return tmp
#     tmp = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
#     w_arr[a][b][c] = tmp
#     return tmp

for i in range(1, 21):
    flag = 0
    for j in range(1,21):
        if j > i : flag = 1
        else : flag = 0
        for k in range(1,21):
            if flag and k > j : 
                w_arr[i][j][k] = w_arr[i][j][k-1] + w_arr[i][j-1][k-1] - w_arr[i][j-1][k]
            else :
                w_arr[i][j][k] = w_arr[i-1][j][k] + w_arr[i-1][j-1][k] + w_arr[i-1][j][k-1] - w_arr[i-1][j-1][k-1]

while (True):
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1 : break 
    if a <= 0 or b <= 0 or c <= 0 : ret = 1
    elif a > 20 or b > 20 or c>20 : ret = w_arr[20][20][20]
    else : ret = w_arr[a][b][c]
    print(f"w({a}, {b}, {c}) = {ret}")