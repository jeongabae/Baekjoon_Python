K = int(input())
for i in range(K):
    P, M = map(int, input().split())
    s = set(input() for i in range(P))
    print(P-len(s))