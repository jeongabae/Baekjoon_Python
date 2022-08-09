N=int(input())
l =list(map(int,input().split()))
print(len(l)-len(set(l)))