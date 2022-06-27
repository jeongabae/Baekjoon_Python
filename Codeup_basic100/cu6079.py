n=int(input())
s=0
for i in range(1,n+1):
    s+=i
    if s>=n:
        print(i)
        break
"""시간은 더 걸리지만 이런 풀이도 있음
n = int(input())
s = 0
t = 0
while s<n :
  t = t+1
  s = s+t  
print(t)

"""