import math
N = list(input())
c = []
for i in range(10):
    c.append(N.count(str(i)))
c[9]=math.ceil((c[6]+c[9])/2)
c[6] = 0
print(max(c))
"""다른분풀이
s=input()
N=[s.count(str(i)) for i in range(10)]
N[6]=(N[6]+N[9]+1)//2;N[9]=N[6]
print(max(N))
"""
"""다른분풀이
n = input()
lst = []
for num in '0123456789':
    lst.append(n.count(num))
lst[6] = (lst[6]+lst[9]+1)//2
del lst[9]
print(max(lst))
"""
