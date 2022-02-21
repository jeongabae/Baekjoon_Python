K = int(input())
n = []
for i in range(K):
    if (a:=int(input()))!= 0:
        n.append(a)
    else:
        n.pop()
print(sum(n))