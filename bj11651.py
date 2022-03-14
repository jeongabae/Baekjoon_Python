N=int(input())
xy=[list(map(int,input().split())) for i in range(N)]
xy.sort(key=lambda x: (x[1], x[0]))
for i in xy:
    print(i[0], i[1])