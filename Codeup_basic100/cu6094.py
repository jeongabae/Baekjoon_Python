n = int(input())
a = sorted(list(map(int,input().split())))
print(a[0])
"""모범답안. 시간 이게 더 길다.
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

min = a[0]
for i in range(0, n) :
  if a[i] < min :
    min = a[i]

print(min)
"""