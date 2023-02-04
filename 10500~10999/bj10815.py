import sys
def input():
    return sys.stdin.readline().rstrip()

def binarysearch(start,end,X,arr):
    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] == X:
            return "1"
        else:
            if arr[mid] > X:
                end = mid - 1
            else:
                start = mid + 1
    return "0"

N=int(input())
arr=list(map(int,input().split()))
arr.sort()
M=int(input())
arr2=list(map(int,input().split()))

for i in arr2:
    print(binarysearch(0,N-1,i,arr),end=" ")
"""이진탐색 안쓰고 아래대로 풀면 시간 초과...!
import sys
def input():
    return sys.stdin.readline().rstrip()

N=int(input())
arr=list(map(int,input().split()))
M=int(input())
arr2=list(map(int,input().split()))

for i in arr2:
    print("1" if i in arr else "0",end=" ")
"""