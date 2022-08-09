t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    r_sum = r1 + r2
    r_difference = abs(r1 - r2)
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == r_sum or d == r_difference:
            print(1)
        elif d < r_sum and d > r_difference:
            print(2)
        else:
            print(0)
