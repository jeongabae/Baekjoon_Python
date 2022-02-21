"""내풀이1
h = [int(input()) for i in range(9)]
spy1 = spy2 = 0
for i in range(8):
    for j in range(i+1,9):
        if sum(h)-h[i]-h[j]==100:
            spy1=h[i]
            spy2=h[j]
h.remove(spy1)
h.remove(spy2)
h.sort()
print(*h, sep="\n")
"""
#3040풀고 다시 풀어본
from itertools import combinations as c
l=sorted(int(input())for i in range(9))
for i in c(l,7):
    if(sum(i)==100):
        for j in i:print(j)
        break
"""다른사람풀이1
l=sorted(int(input())for i in range(9)) #이렇게만 해도 list가 되네..?
for i in l:
 for j in l:
  if i+j==sum(l)-100:
      l.remove(i)
      l.remove(j)
      break
for i in l:
    print(i)
"""
"""다른사람코드 이해해보려고 내가 테스트해본 것
l=sorted(int(input())for i in range(9)) #이렇게만 해도 list가 되네..?
for i in l:
    for j in l:
        print("i",i,"j",j)
        if i+j==sum(l)-100:
            print("remove i", i, "j", j)
            l.remove(i)
            l.remove(j)
            break
        print(l)
for i in l:
    print(i)
"""