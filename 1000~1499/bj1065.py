def count_hansu(n):
    if n < 100:
        hansu = n
    else:
        hansu = 99
        for i in range(100,n+1):
            arr = list(map(int,str(i)))
            if arr[0]-arr[1] == arr[1]-arr[2]:
                hansu += 1
    return hansu
print(count_hansu(int(input())))