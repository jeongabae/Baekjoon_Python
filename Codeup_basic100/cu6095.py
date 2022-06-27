n = int(input())
d = [[0 for x in range(19)] for y in range(19)]
for _ in range(n):
    x, y = map(int,input().split())
    d[x-1][y-1] = 1
for i in range(19):
    print(*d[i])
"""모범답안은 이렇게 풀었음. 이것도 시간이 좀 느림.
d=[]
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')
  print()
"""