a, b = map(int, input().split())
n = []
for i in range(b+1):
    for j in range(i):
        n.append(i)
print(sum(n[a-1:b]))
