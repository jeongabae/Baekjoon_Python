import sys
n,T= map(int,sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
s = 0
cnt = 0
for i in a:
    s+=i
    if s<=T:
        cnt+=1
print(cnt)