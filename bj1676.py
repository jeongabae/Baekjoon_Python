n = int(input())
fac = 1
cnt = 0
while n!=0:
    fac = fac * n
    n -= 1
fac = str(fac)
for i in range(len(fac)-1,0,-1):
    if fac[i]!='0':
        break
    else:
        cnt+=1
print(cnt)
"""조은 풀이
https://suri78.tistory.com/44
"""
"""함수가 이미 있넹...?
from math import factorial
n = int(input())
cnt = 0
for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    cnt += 1
print(cnt)
"""