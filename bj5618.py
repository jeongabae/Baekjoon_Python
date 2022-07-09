import sys
import math

n = int(sys.stdin.readline().rstrip())
s = list(map(int, sys.stdin.readline().rstrip().split()))
g = math.gcd(s[0], math.gcd(s[1], s[-1]))
for i in range(1, (g // 2) + 1):
    if g % i == 0:
        print(i)
print(g)
