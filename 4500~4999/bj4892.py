i = 1
while 1:
    n0 = int(input())
    if n0==0:
        break
    n1 = 3*n0
    if n1%2==0:
        print("%d. even %d" %(i,n0//2))
    else:
        print("%d. odd %d" %(i,(n0-1)//2))
    i+=1
