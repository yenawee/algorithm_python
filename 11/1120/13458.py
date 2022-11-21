N = int(input())

student = list(map(int, input().split()))

B,C = map(int, input().split())

ans = 0
for i in student :
    ans += 1
    if i - B > 0 :
        k = 1 if (i - B) % C else 0
        ans += (i - B) // C + k
print(ans) 