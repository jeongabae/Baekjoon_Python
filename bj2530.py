h, m, s = map(int, input().split())
required_time = int(input())
s += required_time
while s>=60:
    m += 1
    s -= 60
    if m == 60:
        m=0
        h+=1
    if h == 24:
        h = 0
print("%d %d %d"%(h, m, s))
