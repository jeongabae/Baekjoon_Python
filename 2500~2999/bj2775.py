T = int(input())
for _ in range(T):
    floor = int(input())
    unit = int(input())
    apart =[i for i in range(1, unit + 1)] #0층
    for j in range(floor):
        for k in range(1,unit):
            apart[k] += apart[k - 1]
    print(apart[-1]) 