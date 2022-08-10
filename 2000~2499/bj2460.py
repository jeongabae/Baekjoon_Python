a = []
b = 0
for i in range(10):
    c, d = map(int, input().split())
    b -= c
    a.append(b)
    b += d
    a.append(b)
print(max(a))