s = int(input())
tot = 0
N = 0
while s > tot + N:
    N += 1
    tot += N

print(N)