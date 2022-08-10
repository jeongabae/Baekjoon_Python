# nums = list(map(int, input().split()))
# s = 0
# for i in nums:
#     s += i*i
# print(s%10)
"""1등 코드
print(sum(int(a)**2for a in input()[::2])%10)
"""

n = [i*i for i in map(int,input().split())]
print(sum(n)%10)
# print(sum(int(i)**2 for i in input().split())%10)