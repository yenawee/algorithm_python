F,V,C = map(int,input().split())

print(-1) if C <=V else print(int(F / (C-V) + 1))

