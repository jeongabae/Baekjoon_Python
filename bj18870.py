n=int(input())
x=list(map(int,input().split()))
xx=sorted(set(x))
xx={xx[i]:i for i in range(len(xx))}
print(*[xx[i] for i in x])