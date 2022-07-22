d = [[0 for _ in range(10)] for _ in range(10)] #d = [[0]*10 for _ in range(10)]
for i in range(10):
    d[i] = list(map(int,input().split()))
x=y=1
d[x][y]=9
while True:
    if d[x][y]==2:
        d[x][y]=9
        break
    if d[x][y+1]!=1:
        d[x][y]=9
        y+=1
    else:
        if d[x+1][y]!=1:
            d[x][y]=9
            x+=1
        else:
          d[x][y]=9 #이제 못 가는 경우
          break
for i in range(10):
    print(*d[i])
"""모범답안인데 시간이 내 답안보다 좀 더 걸림
m=[]
for i in range(12) :
  m.append([])
  for j in range(12) :
    m[i].append(0)

for i in range(10) :
  a=input().split()
  for j in range(10) :
    m[i+1][j+1]=int(a[j])

x = 2
y = 2
while True :
  if m[x][y] == 0 :
    m[x][y] = 9
  elif m[x][y] == 2 :
    m[x][y] = 9
    break

  if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
    break

  if m[x][y+1] != 1 :
    y += 1
  elif m[x+1][y] != 1 :
    x += 1
    

for i in range(1, 11) :
  for j in range(1, 11) :
    print(m[i][j], end=' ')
  print()
"""