t = int(input())
for i in range(t):
    n = int(input())
    xi = list(map(int,input().split()))
    print((max(xi)-min(xi))*2)