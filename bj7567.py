a = list(input())
h = 10
for i in range(1,len(a)):
    if a[i-1] == a[i]: h += 5
    else: h+=10
print(h)
