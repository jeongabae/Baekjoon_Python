N = int(input())
a = sorted(int(input()) for _ in range(N))
for i in range(N):
    print(a[i])
"""다른분 풀이 빨리풀기 위해 sys사용
import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')
"""