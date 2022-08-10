T = int(input())
for i in range(T):
    n = list(map(int,input().split()))
    s = []
    for j in n:
        if j%2==0:
            s.append(j)
    print(sum(s), min(s))