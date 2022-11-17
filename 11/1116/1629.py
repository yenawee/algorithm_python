A,B,C = map(int, input().split())

def power(A,B,C):
    if B == 1 : return A % C
    if B == 2 : return (A * A) % C
    if B % 2 == 0 : return (power(A, B//2, C)**2) % C
    else : return ((power(A, B//2, C)**2) * A) % C

print(power(A,B,C))