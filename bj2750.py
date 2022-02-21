N = int(input())
n = [int(input()) for i in range(N)]
n.sort()
for i in range(N):
    print(n[i])