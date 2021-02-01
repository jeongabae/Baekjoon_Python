a, b = 1, 1
while not (a == 0 and b == 0):
    a, b = map(int, input().split())
    print(a+b)
