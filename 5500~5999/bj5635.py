"""이게 풀이 1, 밑에꺼가 풀이 2
n = int(input())
a = []
for i in range(n):
    name, d, m, y = input().split()
    d, m, y = map(int, (d,m,y))
    a.append([y,m,d,name])
a.sort()
print(a[-1][3])
print(a[0][3])
"""
n = int(input())
a = []
for i in range(n):
    name, d, m, y = input().split()
    d, m, y = map(int, (d,m,y))
    a.append([name, d, m, y])
a.sort(key=lambda x: (x[3], x[2], x[1]))
print(a[-1][0])
print(a[0][0])

"""cf) 다른 사람 코드
l = [input().split() for i in range(int(input()))]
l.sort(key = lambda x:(int(x[3]), int(x[2]), int(x[1])))
print(l[-1][0],l[0][0],sep='\n')
"""
