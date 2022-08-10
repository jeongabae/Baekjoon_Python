T = int(input())
sieve = [False, False] + [True] * 10000
for i in range(2, 10000):
    if sieve[i]:
        for j in range(2 * i, 10001, i):
            sieve[j] = False
for i in range(T):
    n = int(input())
    a = b = n//2
    for _ in range(n):
        if sieve[a] and sieve[b]:
            print(a, b)
            break
        a -= 1
        b += 1