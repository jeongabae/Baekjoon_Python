T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    n =[str(j).count("0") for j in range(a,b+1)]
    print(sum(n))
