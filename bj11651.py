N=int(input())
xy=[list(map(int,input().split())) for i in range(N)]
xy.sort(key=lambda x: (x[1], x[0]))
for i in xy:
    print(i[0], i[1])
"""다른 사람 코드 
num = int(input())
a = []
for i in range(num):
    [x, y] = map(int, input().split())
    rev = [y, x]
    a.append(rev)
b = sorted(a)
for i in range(num):
    print(b[i][1], b[i][0])
    """