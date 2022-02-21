n = int(input())
X = Y = 100
for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        Y -= x
    elif x < y:
        X -= y
print(X)
print(Y)