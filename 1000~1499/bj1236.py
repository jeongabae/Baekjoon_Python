N,M = map(int,input().split())
board = [input() for _ in range(N)]
row = column = 0

for i in range(N):
    if 'X' not in board[i]:
        row+=1
for j in range(M):
    if 'X' not in [board[k][j] for k in range(N)]: #행과 열은 바꾼 배열의 한 줄 한 줄에 X가 없으면
                                                   #즉, 바꾼 보드에서는 행이지만 원래의 보드에서는 열에 X가 없으면으로 해석됨.
        column+=1
print(max(row,column))

"""다른 사람 풀이 
n,m=map(int,input().split())
a=[input()for i in[0]*n]
print(max(n-sum([1 for i in a if "X"in i]),m-sum([1 for i in range(m)if [1 for j in range(n)if a[j][i]=="X"]])))
"""
"""다른 사람 풀이 
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x = [[i == '.' for i in input().rstrip()] for _ in range(n)]
s = sum(all(y) for y in zip(*x))
t = sum(all(y) for y in x)
print(max(s, t))
"""
"""다른 사람 풀이 : 유명한 풀이 
n,m = map(int,input().split())
arr = [input() for i in range(n)]

row = [0]*n
col = [0]*m
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            row[i] = 1
            col[j] = 1
rCount = 0
for i in row:
    if i == 0:
        rCount += 1
cCount = 0
for j in col:
    if j == 0:
        cCount +=1
print(max(rCount,cCount))

"""