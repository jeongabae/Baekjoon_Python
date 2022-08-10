a = [int(input()) for i in range(8)]
n = []
total = 0
for i in range(5):
    total += max(a)
    index = a.index(max(a))
    n.append(index+1)
    a[index] = -1
n.sort()
print(total)
print(*n)
