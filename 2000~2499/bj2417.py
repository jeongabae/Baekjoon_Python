#[Binary Search] 백준 2417번 : 정수 제곱근
n=int(input())
start=0
end=n
while start<=end:
    mid=(start+end)//2
    if mid**2==n:
        start=mid
        break
    elif mid**2<n:
        start=mid+1
    else:
        end=mid-1
print(start)

"""내장함수 이용 풀이
from math import ceil #올림함수 ceil
n=int(input())
q=ceil(n**0.5)
print(q)
"""
