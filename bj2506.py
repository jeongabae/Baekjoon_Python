#이게 내가 푼 풀이 이면서 문제보고 변수 이해도 가장 되는? 풀
N = int(input())
nums = list(map(int, input().split()))
continue_num = 0
score = 0
for j in nums:
    if j == 0:
        continue_num = 0
    else:
        continue_num += 1
        score += continue_num
print(score)

#밑에 풀이는 최대한 줄여보려고 한 풀이
"""
N=input()
a=b=0
for i in input().split():
    if i=='0':
        a=0
    else:
        a+=1
        b+=a
print(b)
"""
"""이건 시도해보다 린 틀이
N=int(input())
n=list(map(int,input().split()))
a=0
for i in range(0,N):
    print(i)
    if n[i]==0:
        if a>1:
            n[i]=a-1
        a=0
    else:
        a+=1
for i in n:
    print("i출력 ", i)
print(sum(n))
"""

"""이건 다른 분 코드인데 뭐
n=int(input())
a=[0]+list(map(int,input().split()))
for i in range(1,n+1):
	if a[i]:
		a[i]=a[i-1]+1
print(sum(a))
"""



