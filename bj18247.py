t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    if n < 12 or m < 4:
        print(-1)
    else:
        print(1+11*m+3)
