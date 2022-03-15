import sys
N = int(sys.stdin.readline())
xy = [sys.stdin.readline().split() for i in range(N)]
xy.sort(key=lambda x: int(x[0]))
for i in xy:
    print(i[0], i[1])