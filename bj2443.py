"""풀이1
n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))
"""
"""이건 다른 분 풀이
n=int(input())
for i in range(n):
    print(' '*i+'*'*(n-i)+'*'*(n-i-1))
"""
n = int(input())
for i in range(n):
    print(" "*i+"*"*(2*n-(2*(i+1)-1)))