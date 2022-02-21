N = int(input())
arr = list(map(int,input().split()))
print(max(arr)*min(arr))
"""다른사람코드
N=int(input())
data=list(map(int,input().split()))
data.sort()
print(data[0]*data[-1])
"""