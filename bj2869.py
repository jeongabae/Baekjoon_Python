import sys, math
A, B, V = map(int, sys.stdin.readline().split())
day = (V-B)/(A-B)
print(math.ceil(day))
#print(day)//이렇게 하면 틀리는게 4.8일 이면 5일로 출력해야되는데 4로 출력하기 때문..
"""문제그대로 해석 : 시간 오래 걸림 아마 시간초과 날듯?
A, B, V = map(int, input().split())
day = 0

while 1:
    day +=1
    V -= A
    if V<=0:
        break
    V += B
    if V <= 0:
        break
print(day)
"""
