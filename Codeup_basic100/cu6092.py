n = int(input())
a = list(map(int,input().split()))
d = [0]*23
for i in range(n):
  d[a[i]-1] += 1
print(*d)
"""이게 모범답안이라는데 내가 푼 것보다 시간 느림
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

d = []
for i in range(24) :
  d.append(0)

for i in range(n) :
  d[a[i]] += 1

for i in range(1, 24) :
  print(d[i], end=' ')
"""