N=int(input())
xy=sorted([list(map(int,input().split())) for i in range(N)])
for i in range(N):
    print(xy[i][0], xy[i][1])