for _ in range(int(input())):
    a,b=input().split()
    d=[]
    for i in range(len(a)):
        d.append((ord(b[i])-ord(a[i]))%26)
    print("Distances:",*d)