from itertools import combinations as c
n, m = map(int, input().split())
a = list(map(int, input().split()))
a1 = []
for j in c(a, m):
    s = sum(j)
    for k in range(2, s):
        if s % k == 0:
            break
    else:
        if not (s in a1):
            a1.append(s)
a1.sort()
if not a1:
    print(-1)
else:
    print(*a1)
