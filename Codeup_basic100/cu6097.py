h,w = map(int,input().split())
b = [[0 for x in range(w)] for y in range(h)]
n = int(input())
for _ in range(n):
    l,d,x,y = map(int,input().split())
    if d==0:
        for i in range(l):
            b[x-1][y-1+i]=1
    else:
        for i in range(l):
            b[x-1+i][y-1]=1
for i in range(h):
    print(*b[i])
"""모범답안
h,w = input().split()
h = int(h)
w = int(w)

m = []
for i in range(h+1) :
  m.append([])
  for j in range(w+1) :
    m[i].append(0)

n = int(input())
for i in range(n) :
  l,d,x,y = input().split()
  if int(d)==0 :
    for j in range(int(l)) :
      m[int(x)][int(y)+j] = 1
  else :
    for j in range(int(l)) :
      m[int(x)+j][int(y)] = 1

for i in range(1, h+1) :
  for j in range(1, w+1) :
    print(m[i][j], end=' ')
  print()
"""