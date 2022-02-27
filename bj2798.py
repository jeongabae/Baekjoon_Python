from itertools import combinations as c
N, M = map(int,input().split())
l = map(int,input().split())
three = []
for j in c(l,3):
    if(sum(j)<=M):
        three.append(sum(j))
print(max(three))
"""다른 분 코드 
N, M = map(int,input().split())
arr = list(map(int,input().split()))
result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if arr[i]+arr[j]+arr[k]>M:
                continue
            else:
                result=max(result,arr[i]+arr[j]+arr[k])
print(result)
"""