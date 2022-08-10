
"""내풀이
from collections import Counter
n = [int(input())for i in range(10)]
c = Counter(n)
mode = c.most_common(1)
print(int(sum(n)/10))
print(mode[0][0])이
"""
"""다른 사람 풀이 
l=[int(input())for i in [0]*10];print(sum(l)//10,max(set(l),key=l.count))
"""
"""
l = eval('int(input()),'*10)

print(sum(l)//10)
print(max(l, key=l.count))
"""
from collections import Counter
n = [int(input())for i in range(10)]
mode = Counter(n).most_common(1)[0][0]
print(sum(n)//10)
print(mode)
#https://codepractice.tistory.com/71 최빈값 참고