T=int(input())
for i in range(T):
    N = int(input())
    print(sum([i for i in range(1, N + 1) if i % 2]))