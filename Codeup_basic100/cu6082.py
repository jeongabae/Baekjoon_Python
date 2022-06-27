n=int(input())
for i in range(1, n+1):
    a = i%10
    print("X" if a!=0 and a%3==0 else i, end=' ')
"""뭐 이렇게 해도 되긴함(이게 더 느림)
n = int(input())

for i in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9 :
    print("X", end=' ')
  else :
    print(i, end=' ')
"""