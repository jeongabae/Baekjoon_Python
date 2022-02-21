from itertools import combinations as c
l=[int(input()) for i in[0]*9]
for i in c(l,7):
    print(i)
    if(sum(i)==100):
        for j in i:print(j)
        break