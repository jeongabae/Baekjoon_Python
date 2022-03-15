h,m = map(int,input().split())
required_time = int(input())
m += required_time
while m>=60:
    h += 1
    m -= 60
    if h == 24:
        h = 0
print("%d %d"%(h, m))
